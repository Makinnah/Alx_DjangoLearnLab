# notifications/models.py
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications_from')
    verb = models.CharField(max_length=255)  # e.g., "liked", "commented", "followed"
    # Generic relation to the target (post, comment, user, etc.)
    target_ct = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_ct', 'target_id')

    unread = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f'Notification for {self.recipient}: {self.actor} {self.verb} {self.target}'

