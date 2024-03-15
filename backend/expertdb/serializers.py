from rest_framework import serializers

from .models import Doctor, SectionDoctors
from .choices import DoctorTitle, TeacherTitle, TeacherOffice, Degree


class DoctorSerializer(serializers.ModelSerializer):
    doctor_title = serializers.SerializerMethodField()
    teacher_title = serializers.SerializerMethodField()
    teacher_office = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    
    class Meta:
        model = Doctor
        fields = [
            'name',
            'avatar',
            'doctor_title',
            'teacher_title',
            'teacher_office',
            'degree',
            'link',]

    def get_doctor_title(self, obj):
        return DoctorTitle(obj.doctor_title).label

    def get_teacher_title(self, obj):
        return TeacherTitle(obj.teacher_title).label if obj.teacher_title else None

    def get_teacher_office(self, obj):
        return TeacherOffice(obj.teacher_office).label if obj.teacher_office else None

    def get_degree(self, obj):
        return Degree(obj.degree).label if obj.degree else None


class SectionDoctorsSerializer(serializers.ModelSerializer):

    section = serializers.StringRelatedField()
    doctor = DoctorSerializer(read_only=True)
    
    class Meta:
        model = SectionDoctors
        fields = ['section', 'doctor', 'info']
