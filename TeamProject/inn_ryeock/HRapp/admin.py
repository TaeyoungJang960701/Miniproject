
from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_name', 'user_birthdate', 'user_email' ,'user_phone')

admin.site.register(User, UserAdmin)