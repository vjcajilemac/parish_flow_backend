from rest_framework import serializers
from .models import SchoolClass

class SchoolClassSerializer(serializers.ModelSerializer):
    """Serializer for SchoolClass model"""

    class Meta:
        model = SchoolClass
        fields = "__all__"  # Include all fields from the model