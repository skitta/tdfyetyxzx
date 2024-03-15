from django.db import models

from .choices import DoctorTitle, TeacherTitle, TeacherOffice, Degree


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', max_length=8)
    avatar = models.CharField('头像', max_length=25, blank=True, null=True)
    doctor_title = models.CharField('医务职称', max_length=3, choices=DoctorTitle.choices)
    teacher_title = models.CharField('教学职称', max_length=3, choices=TeacherTitle.choices, blank=True, null=True)
    doctor_office = models.CharField('医务职位', max_length=20, blank=True, null=True)
    teacher_office = models.CharField('教学职位', max_length=2, choices=TeacherOffice.choices, blank=True, null=True)
    degree = models.CharField('学历', max_length=3, choices=Degree.choices, blank=True, null=True)
    link = models.URLField('挂号网址', max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta(object):
        verbose_name = '专家库'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'doctor_title')


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='专业组名称')
    doctors = models.ManyToManyField(Doctor, blank=True, through='SectionDoctors', verbose_name='专家')

    def __str__(self):
        return self.name
    
    class Meta(object):
        verbose_name = '专业组'
        verbose_name_plural = verbose_name


class SectionDoctors(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='专业组')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name='专家')
    info = models.TextField('介绍')

    class Meta(object):
        verbose_name = '专业专家'
        verbose_name_plural = verbose_name
        unique_together = ('section', 'doctor')
    
    def __str__(self):
        return f"{self.section.name} - {self.doctor.name}"