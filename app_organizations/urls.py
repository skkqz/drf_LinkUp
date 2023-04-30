from django.urls import path
from .views import OrganizationsAPIView, CreateOrganizationSerializerAPIView

urlpatterns = [
    path('', OrganizationsAPIView.as_view(), name='organizations'),
    path('create', CreateOrganizationSerializerAPIView.as_view(), name='organizations_create'),
]