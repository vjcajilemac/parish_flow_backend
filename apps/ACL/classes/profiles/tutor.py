from django.db import models
from .people import People
class Tutor(People):
    """Representative (parent/guardian) model inheriting from People"""
    
    number_of_children = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Representative"
        verbose_name_plural = "Representatives"