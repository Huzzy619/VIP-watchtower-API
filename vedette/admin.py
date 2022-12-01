from django.contrib import admin
from .models import VIP, History
# Register your models here.
admin.site.register([History, VIP])