from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import json

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


@login_required
def game(request, room_name):
    users = User.objects.all()
    return render(request, 'app/game.html', {'Users': users, 'room_name_json': mark_safe(json.dumps(room_name))})


@login_required
def room(request):
    return render(request, 'app/room.html', {})
