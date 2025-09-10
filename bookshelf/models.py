from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
        ]
