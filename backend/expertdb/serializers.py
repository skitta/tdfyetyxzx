from rest_framework import serializers

from .models import Doctor, SectionDoctors
from .choices import DoctorTitle, TeacherTitle, TeacherOffice, Degree


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def to_representation(self, instance: Doctor):
        ret = super().to_representation(instance)
        ret['doctor_title'] = DoctorTitle(instance.doctor_title).label
        ret['teacher_title'] = TeacherTitle(instance.teacher_title).label if instance.teacher_title else None
        ret['teacher_office'] = TeacherOffice(instance.teacher_office).label if instance.teacher_office else None
        ret['degree'] = Degree(instance.degree).label if instance.degree else None
        return ret


class SectionDoctorsSerializer(serializers.ModelSerializer):

    section = serializers.StringRelatedField()
    doctor = DoctorSerializer(read_only=True)
    
    class Meta:
        model = SectionDoctors
        fields = '__all__'
