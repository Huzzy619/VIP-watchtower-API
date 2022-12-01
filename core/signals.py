from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User, APIKey


@receiver(signal=post_save, sender = User)
def automatic_API_KEY(created, instance, **kwargs):
    if created:
        APIKey.objects.create(user = instance)
