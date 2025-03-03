import uuid
from django.db import models
from django.contrib.auth.models import User
from apps.ACL.enums.ProfileType import ProfileType

class People(models.Model):
    """Base model for all types of people (Student, Teacher, Representative)"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    user = models.OneToOneField(
        User, 
        on_delete=models.SET_NULL, 
        related_name="profile", 
        blank=True, 
        null=True  # User is optional
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    type = models.CharField(
        max_length=15,
        choices=ProfileType.choices,  # Uses ProfileType Enum
        default=ProfileType.STUDENT,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # ✅ This prevents Django from creating a separate "people" table

    def __str__(self):
        return f"{self.name} - {self.get_type_display()}"