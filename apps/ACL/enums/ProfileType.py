from django.db import models

class ProfileType(models.TextChoices):
    STUDENT = "student", "Student"
    TEACHER = "teacher", "Teacher"
    PARENT = "parent", "Parent"
    REOPRESENTATIVE = "representative", "Representative"