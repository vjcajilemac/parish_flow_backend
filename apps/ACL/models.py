import uuid
from django.db import models
from django.contrib.auth.models import User  # Import Django’s built-in User model
from .enums.ProfileType import ProfileType  # Import the Enum choices

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    birthday = models.DateField(blank=True, null=True)

    type = models.CharField(
        max_length=40,
        #choices=ProfileType.choices,  # Use the Enum choices
        default=ProfileType.STUDENT,  # Default profile type
    )

    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name="profile",
        blank=True,
        null=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  #

    def __str__(self):
        return f"{self.user.username} - {self.get_type_display()}"  # Show the user and profile type
    
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        pass
