from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Organizations
from .serializers import OrganizationSerializer, CreateOrganizationSerializer


class OrganizationsAPIView(ListAPIView):

    """
    Представление для организаций.
    """

    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer


class CreateOrganizationSerializerAPIView(CreateAPIView):

    """
    Представление для создания организации.
    """

    serializer_class = CreateOrganizationSerializer
    permission_classes = [IsAuthenticated]
