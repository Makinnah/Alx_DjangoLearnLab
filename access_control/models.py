from django.db import models
from django.contrib.auth import get_user_model

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view resource"),
            ("can_create", "Can create resource"),
            ("can_edit", "Can edit resource"),
            ("can_delete", "Can delete resource"),
        ]
