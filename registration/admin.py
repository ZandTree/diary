from django.contrib import admin
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','created_at','age','location']

admin.site.register(Profile,UserProfileAdmin)
