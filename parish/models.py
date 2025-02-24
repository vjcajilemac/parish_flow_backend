from django_tenants.models import TenantMixin, DomainMixin
from django.db import models

# Create your models here.
class Parish(TenantMixin):
    name = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True  # Automatically create schema when saving

class Domain(DomainMixin):
    pass