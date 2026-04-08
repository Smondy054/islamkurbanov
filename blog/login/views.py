from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'base.html')


def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def add_user(request):
    if request.method == "POST":
    #получаем данные из формы 
        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('/users/')
    # это просто запрос, нужно покаать форму
    else:
       form = UserForm()
    return render(request, "add_user.html", {'form':form})
        
