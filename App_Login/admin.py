from django.contrib import admin

from App_Login.models import UserProfile
from .models import*
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Follow)

