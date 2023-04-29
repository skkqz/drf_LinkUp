from rest_framework.generics import ListAPIView
from .models import Organizations
from .serializers import OrganizationSerializer


class OrganizationsAPIView(ListAPIView):

    """
    Представление для организаций.
    """

    queryset = Organizations.objects.all()
    serializer_class = OrganizationSerializer
