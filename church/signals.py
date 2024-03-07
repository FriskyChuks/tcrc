from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FundRequest, FundRequestApproval


@receiver(post_save, sender=FundRequestApproval)
def post_save_update_sub_total(sender, instance, created, **kwargs):
    if created:
        FundRequest.objects.filter(id=instance.request.id).update(approval=True)