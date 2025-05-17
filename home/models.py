from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    difficulty = models.CharField(max_length=10)  # easy/medium/hard
    title = models.CharField(max_length=100)
    description = models.TextField()
    expected_output = models.TextField()

class BattleRoom(models.Model):
    room_name = models.CharField(max_length=50, unique=True)
    player1 = models.ForeignKey(User, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, related_name='player2', on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=10)
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.SET_NULL, null=True, blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    time_limit = models.IntegerField(default=20)  # in minutes
    is_active = models.BooleanField(default=True)
