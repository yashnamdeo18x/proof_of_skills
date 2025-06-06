from django.shortcuts import render
import requests
from django.http import JsonResponse,HttpResponse
from social_django.models import UserSocialAuth
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.conf import settings
import json
import random
from .models import BattleRoom, Question
from django.contrib.auth.models import User





def landing(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    print("DEBUG: Logging in with redirect URI → /complete/github/")

    return render(request, 'home.html', {'user': request.user})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # this logs the user out of Django session
    return redirect('/landing.html')  # or redirect to your login page


@login_required
def get_repos(request):
    try:
        user_social = UserSocialAuth.objects.get(user=request.user, provider='github')
        access_token = user_social.extra_data['access_token']
        headers = {'Authorization': f'token {access_token}'}

        # Fetch repos
        repo_list = []
        repos_response = requests.get('https://api.github.com/user/repos', headers=headers)

        if repos_response.status_code == 200:
            repos = repos_response.json()
            for repo in repos:
                name = repo['name']
                created = repo['created_at']
                owner = repo['owner']['login']

                # Languages API
                lang_url = f"https://api.github.com/repos/{owner}/{name}/languages"
                lang_res = requests.get(lang_url, headers=headers)
                raw_lang = lang_res.json() if lang_res.status_code == 200 else {}
                
                # Convert to percentages
                total = sum(raw_lang.values())
                languages_percentages = {}

                for lang, count in raw_lang.items():
                    if total > 0:
                        percent = (count / total) * 100
                        languages_percentages[lang] = f"{percent:.1f}%"
                 
                # Contents API (files)
                files_url = f"https://api.github.com/repos/{owner}/{name}/contents"
                files_res = requests.get(files_url, headers=headers)
                files_data = files_res.json() if files_res.status_code == 200 else []
                
                # Separate folders and files
                folders = []
                files = []

                for f in files_data:
                    if f['type'] == 'dir':
                        folders.append(f"📁 {f['name']}/")
                    elif f['type'] == 'file':
                        files.append(f"📄 {f['name']}")

# Combine folders first, then files
                file_items = folders + files
                # Combine all
                repo_list.append({
                    'name': name,
                    'created': created,
                    'languages': languages_percentages,
                    'files': file_items
                })

            return render(request, 'home.html', {'repos': repo_list, 'user': request.user})

        else:
            return JsonResponse({'error': 'GitHub repo fetch failed'}, status=repos_response.status_code)

    except UserSocialAuth.DoesNotExist:
        return JsonResponse({'error': 'GitHub not connected'}, status=400)


from .utils import calculate_repo_score, get_score_input  # Use the scoring + helper logic

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from django.shortcuts import render, redirect
import requests

@csrf_exempt
@login_required
def verify_repo(request):
    if request.method == "POST":
        repo_name = request.POST.get("repo_name")
        username = request.user.username
        email = request.user.email

        try:
            # GitHub token
            social = UserSocialAuth.objects.get(user=request.user, provider='github')
            token = social.extra_data['access_token']
            headers = {'Authorization': f'token {token}'}

            owner = username
            base_url = f"https://api.github.com/repos/{owner}/{repo_name}"

            # === REPO INFO ===
            repo_res = requests.get(base_url, headers=headers)
            try:
                repo_data = repo_res.json()
                # Catch GitHub error like {"message": "Not Found"}
                if not isinstance(repo_data, dict) or 'created_at' not in repo_data:
                    return render(request, 'error.html', {'message': 'Repository not found or inaccessible.'})
            except Exception:
                return render(request, 'error.html', {'message': 'Failed to fetch repository information.'})

            # === COMMITS ===
            commits_res = requests.get(f"{base_url}/commits", headers=headers)
            try:
                commits_data = commits_res.json()
                commits = commits_data[:100] if isinstance(commits_data, list) else []
            except Exception:
                commits = []

            # === CONTRIBUTORS ===
            contributors_res = requests.get(f"{base_url}/contributors", headers=headers)
            try:
                contributors_data = contributors_res.json()
                contributors = contributors_data if isinstance(contributors_data, list) else []
            except Exception:
                contributors = []

            # === FILES ===
            files_res = requests.get(f"{base_url}/contents", headers=headers)
            try:
                files_data = files_res.json()
                files = files_data if isinstance(files_data, list) else []
            except Exception:
                files = []

            file_count = len(files)

            # === PREPARE DATA FOR SCORING ===
            github_data = {
                "repo": repo_data,
                "commits": commits,
                "contributors": contributors,
                "files": files,
                "file_count": file_count
            }

            score_input = get_score_input(github_data, username, email)
            result = calculate_repo_score(score_input)
            
            request.session["score"] = result["score"]
            request.session["verdict"] = result["verdict"]
            request.session["repo_name"] = repo_name
            
            return render(request, 'score.html', {
                'repo': repo_name,
                'score': result['score'],
                'verdict': result['verdict'],
                'show_mint': result['score'] >= 60
            })

        except Exception as e:
            print("🔴 Verification Error:", str(e))  # Optional debug log
            return render(request, 'error.html', {'message': str(e)})

    return redirect('home')    


@csrf_exempt
@login_required
def mint_nft(request):
    # You'll build this part later
    
    request.session.pop("score", None)
    return HttpResponse("Minting NFT... coming soon!")


@csrf_exempt
@login_required
def nft_metadata(request, repo):
    user = request.user
    username = user.username
    email = user.email

    # Fetch score from session
    score = request.session.get("score", 0)
    
    
    
    image_url = f"https://api.dicebear.com/7.x/bottts/svg?seed={username}"

    metadata = {
        "name": f"Proof of Skill NFT - {repo}",
        "description": f"Verified skill badge for {username} based on GitHub repo '{repo}'.",
        "image": image_url,
        "attributes": [
            {"trait_type": "Developer", "value": username},
            {"trait_type": "Score", "value": score},
            {"trait_type": "Repository", "value": repo},
            {"trait_type": "Verified By", "value": "GITProofiX"},
        ]
    }

    return JsonResponse(metadata)



def get_random_question(difficulty):
    questions = Question.objects.filter(difficulty=difficulty)
    if questions.exists():
        return random.choice(list(questions))
    else:
        raise ValueError(f"No questions found for difficulty '{difficulty}'")


from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def start_battle_form(request):
    return render(request, 'start_battle.html')

@login_required
def start_battle(request):
    difficulty = request.POST.get("difficulty")  # easy/medium/hard
    user = request.user

    # Check if there's a waiting room with same difficulty
    waiting_room = BattleRoom.objects.filter(player2__isnull=True, difficulty=difficulty, is_active=True).exclude(player1=user).first()

    if waiting_room:
        # Join existing room
        waiting_room.player2 = user
        waiting_room.save()
        return redirect(f'/battle/{waiting_room.room_name}/')
    else:
        # Create a new room
        room_name = get_random_string(12)

        try:
            question = get_random_question(difficulty)
        except ValueError as e:
            return HttpResponse(str(e))  # Handles case when no question found

        time_limit = {'easy': 20, 'medium': 30, 'hard': 40}.get(difficulty, 20)

        room = BattleRoom.objects.create(
            room_name=room_name,
            player1=user,
            difficulty=difficulty,
            question=question,
            time_limit=time_limit,
        )
        return redirect(f'/battle/{room_name}/')

def challenge_user(request):
    github_username = request.POST.get("github_username")
    difficulty = request.POST.get("difficulty")
    user = request.user

    try:
        opponent = User.objects.get(username=github_username)
    except User.DoesNotExist:
        return HttpResponse("User not found")

    room_name = get_random_string(12)
    question = get_random_question(difficulty)
    time_limit = {'easy': 20, 'medium': 30, 'hard': 40}.get(difficulty, 20)

    room = BattleRoom.objects.create(
        room_name=room_name,
        player1=user,
        player2=opponent,
        difficulty=difficulty,
        question=question,
        time_limit=time_limit,
    )
    return redirect(f'/battle/{room_name}/')

def battle_room_view(request, room_name):
    room = get_object_or_404(BattleRoom, room_name=room_name)
    return render(request, 'battle_room.html', {
        'room': room,
        'user': request.user
    })
