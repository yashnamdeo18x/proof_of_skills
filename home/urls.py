from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # ← default landing page
    path('home/', views.home, name='home'),
    path('api/repos/', views.get_repos, name='get_repos'),  # ✅ new
    path('verify-repo/', views.verify_repo, name='verify_repo'),
    path('landing/', views.landing, name='landing'),  # ← default landing page
]
