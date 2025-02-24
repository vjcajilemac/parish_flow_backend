from django_tenants.utils import schema_context
from django.http import JsonResponse
from parish.models import Parish
from django.apps import apps  # 🔹 Ensures Django is fully loaded

class TenantHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Ensure Django is fully loaded before accessing models
        if not apps.ready:
            return JsonResponse({"error": "Django is not fully loaded yet"}, status=500)
        
        host_parts = request.get_host().split('.')
        
        # Handle central (public) requests
        if len(host_parts) == 1 or host_parts[0] in ["localhost", "127"]:
            request.is_central = True
            return self.get_response(request)

        # Extract tenant from subdomain (example: parish1.localhost)
        subdomain = host_parts[0]

        try:
            tenant = Parish.objects.get(schema_name=subdomain)
            request.tenant = tenant  # Attach tenant to request
        except Parish.DoesNotExist:
            return JsonResponse({"error": "Tenant not found"}, status=404)

        # Switch to the correct schema
        with schema_context(tenant.schema_name):
            response = self.get_response(request)

        return response