import logging
from rest_framework import viewsets

from .serializers import SectionDoctorsSerializer
from .models import SectionDoctors


logger = logging.getLogger('log')


class SectionDoctorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SectionDoctors.objects.all()
    serializer_class = SectionDoctorsSerializer
