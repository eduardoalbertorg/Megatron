from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Employee


"""
@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        print("Esto es lo que dice la instancia {}".format(instance))
        # Employee.objects.create(user=instance)
"""


"""
@receiver(post_save, sender=User)
def save_employee(sender, instance, **kwargs):
    # instance.employee.save()
    print("Esta es la instancia {}".format(instance))
"""