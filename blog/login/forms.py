from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'age']
        labels = {
            'login' : 'Логин',
            'passsword' : 'Пароль',
            'first_name' : 'Имя',
            'ast_name' : 'Фамилия',
            'age' : 'Возвраст',
        } 