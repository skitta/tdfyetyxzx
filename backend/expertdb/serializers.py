from rest_framework import serializers

from .models import Doctor, SectionDoctors


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance: Doctor):
        ret =  super().to_representation(instance)
        ret['doctor_title'] = next((t[1] for t in instance.DoctorTitle.choices if instance.doctor_title in t), None)
        ret['teacher_title'] = next((t[1] for t in instance.TeacherTitle.choices if instance.teacher_title in t), None)
        ret['teacher_office'] = next((t[1] for t in instance.TeacherOffice.choices if instance.teacher_office in t), None)
        ret['degree'] = next((t[1] for t in instance.Degree.choices if instance.degree in t), None)
        return ret


class SectionDoctorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SectionDoctors
        fields = '__all__'
    
    def to_representation(self, instance: SectionDoctors):
        ret =  super().to_representation(instance)
        ret['section'] = instance.section.name
        ret['doctor'] = DoctorSerializer(instance.doctor).data
        return ret
