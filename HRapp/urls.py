from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView , name='home'),
    path('login/', views.LoginView , name='login'),
    path('signup/', views.SignupView , name='signup'),
    path('members/', views.MembersView, name='members'),  
    path('members/<int:user_id>/', views.MembersDetailView, name='member_detail'),
    path('members/me', views.MeView, name='me_detail'),
    path('logout/', views.LogoutView, name='logout'),
    path('members/me/edit/', views.MeEditView, name='me_edit'),
    path('members/me/edit/image', views.MeImageView, name='me_edit_image'),
    path('intro/', views.intro, name='intro'),
    path('members/', views.members, name='members'),
    path('minigame/', views.minigame, name='minigame'),  # ✅ 추가된 라인

    path('minesweeper/', views.minesweeperView, name='minesweeper'),
]
