from django.db import models

# Create your models here.

class Level(models.Model):
    """Model definition for Level."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Level."""

        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

    def __str__(self):
        """Unicode representation of Level."""
        pass


class Period(models.Model):

   
 
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()

    def formatted_start(self):
        return self.start_date.strftime('%B %Y')  # "January 2024"

    def formatted_end(self):
        return self.end_date.strftime('%B %Y')  # "December 2024"

    def __str__(self):
        return f"{self.formatted_start()} - {self.formatted_end()}"
    
class SchoolClass(models.Model):

    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("completed", "Completed"),
    ]
     
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=5)
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.start_hour.strftime('%I:%M %p')} to {self.end_hour.strftime('%I:%M %p')}"
    

    