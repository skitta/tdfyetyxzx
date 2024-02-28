from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = '__all__'

    def to_representation(self, instance: Doctor):
        ret =  super().to_representation(instance)
        ret['doctor_title'] = next((t[1] for t in instance.DoctorTitle.choices if instance.doctor_title in t), None)
        ret['teacher_title'] = next((t[1] for t in instance.TeacherTitle.choices if instance.teacher_title in t), None)
        ret['degree'] = next((t[1] for t in instance.Degree.choices if instance.degree in t), None)
        ret['major'] = [m.name for m in instance.major.all()]
        ret['avatar'] = instance.get_avatar_url()
        ret['schedule'] = [s.display() for s in instance.schedule.all()]
        return ret
