from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

from django.contrib.auth.models import User
def home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/home.html', {'users': users})

def chatroom(request, username):
    return render(request, 'chat/chatroom.html', {'username': username})

