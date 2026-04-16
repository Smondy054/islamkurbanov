from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'login', 'first_name', 'last_name', 'age', 'balance']
    search_fields = ['login', 'first_name', 'last_name']