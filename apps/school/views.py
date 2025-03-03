from django.shortcuts import render
from rest_framework import viewsets
from .models import SchoolClass
from .serializers import SchoolClassSerializer
# Create your views here.

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer