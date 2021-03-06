from django.contrib import admin
from .models import Profile, PhoneDb
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile, ProfileAdmin)

class PhoneDBAdmin(admin.ModelAdmin):
    list_display = ["user","phone","is_verified"]

admin.site.register(PhoneDb, PhoneDBAdmin)