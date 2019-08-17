from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='app-register'),
    path('room/<str:room_name>/', views.game, name='app-game'),
    path('room', views.room, name='app-room'),
]