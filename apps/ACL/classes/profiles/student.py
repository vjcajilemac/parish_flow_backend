from django.db import models
from .people import People

class Student(People):
    """Student model inheriting from People"""
    
    grade = models.CharField(max_length=20, blank=True, null=True)
    

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
