from django.db import models
from .people import People
class Teacher(People):
    """Teacher model inheriting from People"""
    
    subject = models.CharField(max_length=100, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"