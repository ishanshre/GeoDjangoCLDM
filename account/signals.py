from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Employee, Profile

User = get_user_model()


@receiver(signal=post_save, sender=User)
def save_tables(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        if instance.is_customer:
            Customer.objects.get_or_create(user=instance)
        elif instance.is_employee:
            Employee.objects.get_or_create(user=instance)
