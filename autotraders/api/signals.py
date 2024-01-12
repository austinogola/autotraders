# bidders/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Bidder

@receiver(post_save, sender=Bidder)
def bidder_post_save(sender, instance, created, **kwargs):
    if created:
        # Code to execute when a Bidder is added
        print(f'Bidder {instance} added!')

@receiver(post_delete, sender=Bidder)
def bidder_post_delete(sender, instance, **kwargs):
    # Code to execute when a Bidder is deleted
    print(f'Bidder {instance} deleted!')
