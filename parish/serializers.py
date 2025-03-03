from rest_framework import serializers
from parish.models import Parish

class TenantSerializer(serializers.Serializer):
    """Serializer for tenant validation"""
    name = serializers.CharField(
        max_length=50,
        error_messages={
            "blank": "The schema_name field cannot be empty.",
            "required": "You must provide a schema_name.",
            "max_length": "The schema_name must be at most 50 characters."
        }
    )
    domain = serializers.CharField(
        max_length=100,
        error_messages={
            "blank": "The domain field cannot be empty.",
            "required": "You must provide a domain.",
            "max_length": "The domain must be at most 100 characters."
        }
    )

    def validate_name(self, value):
        """Ensure schema_name is unique"""
        if Parish.objects.filter(name=value).exists():
            raise serializers.ValidationError("Tenant already exists.")
        return value