from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # ← default landing page
    path('dashboard/', views.home, name='home'),
    path('api/repos/', views.get_repos, name='get_repos'),  # ✅ new
]
