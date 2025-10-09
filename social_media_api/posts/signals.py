# posts/signals.py
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, m2m_changed
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from .models import Like, Post
from notifications.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        # do not notify if the liker is the post author
        if post.author and post.author.pk != instance.user.pk:
            Notification.objects.create(
                recipient=post.author,
                actor=instance.user,
                verb='liked your post',
                target_ct=ContentType.objects.get_for_model(post),
                target_id=post.id
            )

@receiver(post_delete, sender=Like)
def delete_like_notification(sender, instance, **kwargs):
    # Optionally delete the like notification when the like is removed
    post = instance.post
    Notification.objects.filter(
        recipient=post.author,
        actor=instance.user,
        verb='liked your post',
        target_ct=ContentType.objects.get_for_model(post),
        target_id=post.id
    ).delete()
