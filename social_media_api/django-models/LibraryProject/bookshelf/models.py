from django.db import models
from relationship_app.models import CustomUser  # assuming this is your user model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
