from django.shortcuts import render, redirect
from .models import User
from .froms import UserForm

def add_user(request):
    if request.method == 'POST':
        #получим данные. нужно сохранить юзера в базу
        if request.method == "POST":
            #получаем данные из формы 
            user = UserForm(request.POST)
            if user.is_valid():
                user.save()
            return redirect('/')
        # это просто запрос, нужно покаать форму
        else:
            form = UserForm()
            return render(request, "add_user.html", {'form':form})
        
