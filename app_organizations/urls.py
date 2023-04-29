from django.urls import path
from .views import OrganizationsAPIView

urlpatterns = [
    path('organizations/', OrganizationsAPIView.as_view(), name='organizations'),

]