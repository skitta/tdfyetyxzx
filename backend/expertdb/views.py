import logging
from rest_framework import viewsets

from .serializers import DoctorSerializer
from .models import Doctor


logger = logging.getLogger('log')


class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

