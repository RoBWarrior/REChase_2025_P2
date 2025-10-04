from django.urls import path, include
from . import views

app_name = 'teams'
urlpatterns = [
    path('', views.home, name='home'),
    path('get_team/', views.get_team, name='get-team'),
    path('create-team/', views.createTeam, name='create-team'),
    path('join-team/', views.joinTeam, name='join-team'),
    path('accept-team-mate/', views.acceptTeamMateView, name='accept-teammate'),
    path('complete-profile/', views.profileCompleteView, name='complete-profile'),
    path('scoreboard/', views.leaderboard_submissions, name='scoreboard'),
    path('rules/', views.rules, name='rules'),
    path('playerdetail/', views.playerdetail, name='teamdetail'),
    path('detailedscore/',views.detailedScoreboardView, name='detailedscore'),
    path('chase/', views.get_level, name='get-level'),
    path('chase/1/', views.start_hunt, name='start_hunt'),
    path('submit/', views.submit_solution, name='submit-solution'),
    path('create-admin-player/', views.create_admin_player, name='create-admin-player'),
]
