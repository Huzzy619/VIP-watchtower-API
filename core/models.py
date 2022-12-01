from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import create_api_key
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)


class APIKey(models.Model):
    key = models.CharField(max_length=60, default=create_api_key, unique=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="keys")


    def save(self, **kwargs):
        while  APIKey.objects.filter(key = self.key):
            self.key = create_api_key()
        
        return super().save(**kwargs)

