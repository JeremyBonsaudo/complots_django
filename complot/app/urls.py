from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='app-register'),
    path('game', views.game, name='app-game'),
]