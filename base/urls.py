from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('update-user/', views.updateUser, name='update-user'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('<int:id>', views.view_habit, name='view_habit'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('<int:id>', views.view_completed_dates, name='view_completed_dates'),
    path('<int:id>', views.view_inactivity_dates, name='view_inactivity_dates'),

    path('check_off/<int:id>', views.check_off, name='check_off'),
]
