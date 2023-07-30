from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Author


@receiver(post_save, sender=Author)
def update_table(sender, instance, created, **kwargs):
    if created:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        group_name = 'table-notification'
        event = {
            "type": "row_created",
            "data": instance
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
    else:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        group_name = 'table-notification'
        event = {
            "type": "row_updated",
            "data": instance
        }
        async_to_sync(channel_layer.group_send)(group_name, event)


@receiver(post_delete, sender=Author)
def delete_row(sender, instance, **kwargs):
    print(f"we deleted {instance.id}")
    # trigger notification to all consumers in the 'user-notification' group
    channel_layer = get_channel_layer()
    group_name = 'table-notification'
    event = {
        "type": "row_deleted",
        "data": instance
    }
    async_to_sync(channel_layer.group_send)(group_name, event)