from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class VIP(models.Model):
    name = models.CharField(max_length=550)
    occupation = ArrayField(models.CharField(max_length=200, null= True, blank=True))
    networth = models.BigIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    vip_score = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    
    # def save(self, *args, **kwargs):
    #     if not self.vip_score:
    #         self.vip_score = 10
    #     return super().save(self.vip_score, **kwargs)


class History(models.Model):
    name = models.CharField(max_length=550)
    result = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='history')