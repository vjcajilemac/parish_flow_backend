from django.urls import path
#from parish.views import create_tenant
from parish.views import TenantCreateAPIView

urlpatterns = [
    #path("create_tenant", create_tenant),  # API to create new tenants
     path("create_tenant", TenantCreateAPIView.as_view(), name="create_tenant"),
]