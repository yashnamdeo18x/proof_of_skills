import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import BattleRoom, Question
from django.contrib.auth.models import User
from asgiref.sync import database_sync_to_async
import aiohttp

class BattleConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'battle_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get('type')

        if event_type == 'submit_code':
            code = data.get('code')
            username = data.get('username')

            # Load room and expected output
            room = await database_sync_to_async(BattleRoom.objects.get)(room_name=self.room_name)

            # Only process if no winner yet
            if room.winner_id is None:
                is_correct = await self.evaluate_code(code, room.question.expected_output)

                if is_correct:
                    room.winner = await database_sync_to_async(User.objects.get)(username=username)
                    room.is_active = False
                    await database_sync_to_async(room.save)()

                    await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'battle_message',
                            'message': {
                                'type': 'winner',
                                'username': username,
                            }
                        }
                    )

    async def battle_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    async def evaluate_code(self, code, expected_output):
        JUDGE0_URL = "https://judge0-ce.p.rapidapi.com/submissions"
        headers = {
            "X-RapidAPI-Key": "<YOUR_RAPID_API_KEY>",
            "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com",
            "content-type": "application/json"
        }
        payload = {
            "language_id": 71,  # Python 3
            "source_code": code,
            "expected_output": expected_output.strip(),
            "stdin": ""
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(JUDGE0_URL + "?base64_encoded=false&wait=true", json=payload, headers=headers) as resp:
                result = await resp.json()
                return result.get("status", {}).get("description") == "Accepted"
