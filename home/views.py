from django.shortcuts import render
import requests
from django.http import JsonResponse
from social_django.models import UserSocialAuth
from django.contrib.auth.decorators import login_required

@login_required



def landing(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html', {'user': request.user})


@login_required
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
