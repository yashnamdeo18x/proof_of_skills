from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # ← default landing page
    path('home/', views.home, name='home'),
    path('api/repos/', views.get_repos, name='get_repos'),  # ✅ new
    path('verify-repo/', views.verify_repo, name='verify_repo'),
    path('landing/', views.landing, name='landing'),  # ← default landing page
    path("__reload__/", include("django_browser_reload.urls")),
    path('mint-nft/', views.mint_nft, name='mint_nft'),
    path('nft/metadata/<str:repo>/', views.nft_metadata, name='nft_metadata'),
    path('logout/', views.logout_view, name='logout'),
    path('battle/start/', views.start_battle_form, name='start-battle-form'),
    path('start_battle/', views.start_battle, name='start_battle'),
    path('challenge_user/', views.challenge_user, name='challenge_user'),
    path('battle/<str:room_name>/', views.battle_room_view, name='battle-room'),
   
]