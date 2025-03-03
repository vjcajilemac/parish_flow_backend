from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from parish.models import Parish, Domain
from parish.serializers import TenantSerializer

class TenantCreateAPIView(APIView):
    """API to create a new tenant (parish)"""

    def post(self, request):
        """Validate input and create a new tenant"""
        serializer = TenantSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = serializer.validated_data["name"]
        domain_url = serializer.validated_data["domain"]

        try:
            # Create the tenant
            tenant = Parish(name=name, schema_name=f"parish-{domain_url}")
            tenant.save()

            # Assign a domain to the tenant
            domain = Domain(domain=domain_url, tenant=tenant)
            domain.save()

            return Response({"message": "Tenant created successfully", "tenant": name, "domain": domain_url}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        """List all tenants"""
        tenants = Parish.objects.all().values("schema_name", "name")
        return Response(list(tenants), status=status.HTTP_200_OK)



"""
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from parish.models import Parish, Domain
from django.http import JsonResponse
import json
# Create your views here.
@csrf_exempt  # Disable CSRF for simplicity (use proper authentication in production)
def create_tenant(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests allowed"}, status=405)

    try:
        data = json.loads(request.body)  # Parse JSON input
        schema_name = data.get("schema_name")  # e.g., "parish1"
        domain_url = data.get("domain")  # e.g., "parish1.localhost"

        if not schema_name or not domain_url:
            return JsonResponse({"error": "Missing schema_name or domain"}, status=400)

        # Check if tenant already exists
        if Parish.objects.filter(schema_name=schema_name).exists():
            return JsonResponse({"error": "Tenant already exists"}, status=400)

        # Create the new tenant
        tenant = Parish(schema_name=schema_name, name=f"Parish {schema_name}")
        tenant.save()  # This automatically creates the schema

        # Assign a domain to the tenant
        domain = Domain(domain=domain_url, tenant=tenant)
        domain.save()

        return JsonResponse({"message": "Tenant created successfully", "tenant": schema_name, "domain": domain_url}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
"""