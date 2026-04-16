from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from functools import wraps

# Декоратор для проверки авторизации
def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'user_id' not in request.session:
            return redirect('/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


def index(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    
    context = {
        'login': request.session.get('user_login', 'Гость')
    }
    return render(request, 'index.html', context)


def login_view(request):
    # Если пользователь уже авторизован, перенаправляем на главную
    if 'user_id' in request.session:
        return redirect('/')
        
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        login = request.POST.get('login')
        password = request.POST.get('pas')
        
        try:
            user = User.objects.get(login=login, password=password)
            request.session['user_id'] = user.id
            request.session['user_login'] = user.login
            return redirect('/')
        except User.DoesNotExist:
            return render(request, 'login.html', {
                'error': 'Неверный логин или пароль'
            })


def logout_view(request):
    request.session.flush()
    return redirect('/login/')


@login_required
def home(request):
    return render(request, 'base.html')


@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


# Убираем @login_required - регистрация доступна всем
def add_user(request):
    # Если пользователь уже авторизован, перенаправляем на главную
    if 'user_id' in request.session:
        return redirect('/')
        
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # После регистрации сразу авторизуем пользователя
            request.session['user_id'] = user.id
            request.session['user_login'] = user.login
            return redirect('/')
    else:
        form = UserForm()
    return render(request, "add_user.html", {'form': form})