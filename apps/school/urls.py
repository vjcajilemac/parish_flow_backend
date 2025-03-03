from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SchoolClassViewSet

router = DefaultRouter()
router.register(r'classes', SchoolClassViewSet)  # Generates all CRUD routes

urlpatterns = [
    path("", include(router.urls)),  # Includes all auto-generated API endpoints
]