from django.contrib import admin

# Register your models here.
from Lead.models import User, Profile, Profile

admin.site.register(User)
admin.site.register(Profile)
