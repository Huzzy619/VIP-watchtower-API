from django.contrib import admin
from .models import APIKey, User
# Register your models here.

admin.site.register([APIKey, User])
