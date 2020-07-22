from alarm_clock.models import AlarmClock
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=AlarmClock)
def notify_new_alarm(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gossip", {"type": "alarm.gossip",
                       "event": "New Alarm",
                       "title": instance.title}
        )