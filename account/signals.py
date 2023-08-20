from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Customer, Employee, Profile

User = get_user_model()


@receiver(signal=post_save, sender=User)
def save_tables(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()
        if instance.is_customer:
            customer = Customer.objects.create(user=instance)
            customer.save()
        elif instance.is_employee:
            employee = Employee.objects.create(user=instance)
            employee.save()
