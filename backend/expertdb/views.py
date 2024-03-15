from rest_framework import viewsets

from .serializers import SectionDoctorsSerializer
from .models import SectionDoctors


class SectionDoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SectionDoctors.objects.all()
    serializer_class = SectionDoctorsSerializer
