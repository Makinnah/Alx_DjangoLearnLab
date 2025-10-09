# accounts/signals.py
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from django.conf import settings

User = settings.AUTH_USER_MODEL  # string; for queries use get_user_model()

# This only works if you use a ManyToMany relationship on the user model named `following`.
@receiver(m2m_changed, sender=get_user_model().following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    # instance is the user whose following changed
    if action == 'post_add':
        for followed_pk in pk_set:
            followed = get_user_model().objects.get(pk=followed_pk)
            # notify the followed user that instance followed them
            Notification.objects.create(
                recipient=followed,
                actor=instance,
                verb='followed you',
                # target could be the `instance` (actor) but optional
                target_ct=ContentType.objects.get_for_model(instance),
                target_id=instance.pk
            )
    if action == 'post_remove':
        for unfollowed_pk in pk_set:
            unfollowed = get_user_model().objects.get(pk=unfollowed_pk)
            Notification.objects.filter(
                recipient=unfollowed,
                actor=instance,
                verb='followed you'
            ).delete()
