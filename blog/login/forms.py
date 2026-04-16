from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    
    class Meta:
        model = User
        fields = ['login', 'password', 'first_name', 'last_name', 'age']
        labels = {
            'login': 'Логин',
            'password': 'Пароль',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age': 'Возраст',
        }
    
    def clean_login(self):
        login = self.cleaned_data.get('login')
        if User.objects.filter(login=login).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует')
        return login