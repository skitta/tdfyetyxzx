import os

from django.db import models
from django.utils.translation import gettext_lazy as _


class Doctor(models.Model):

    class DoctorTitle(models.TextChoices):
        ATTENDING_PHYSICIAN = 'AP', _('主任医师')
        ASSOCIATE_ATTENDING_PHYSICIAN = 'AAP', _('副主任医师')
        CHIEF_RESIDENT = 'CR', _('主治医师')

    class TeacherTitle(models.TextChoices):
        PROFESSOR = 'PR', _('教授')
        ASSOCIATE_PROFESSOR = 'APR', _('副教授')

    class TeacherOffice(models.TextChoices):
        MasterTutor = 'MT', _('硕导')
        DoctorTutor = 'DT', _('博导')

    class Degree(models.TextChoices):
        BACHELOR_MEDICINE = 'MB', _('医学学士')
        MASTER_MEDICINE = 'MM', _('医学硕士')
        DOCTOR_MEDICINE = 'MD', _('医学博士')
        POSTDOCTOR_MEDICINE = 'MPD', _('医学博士后')
    
    def user_directory_path(instance, filname:str):
        ext = filname.split('.').pop()
        filename = '{0}.{1}'.format(instance.id, ext)
        return os.path.join('avatar', filename)

    id = models.AutoField
    name = models.CharField('姓名', max_length=8)

    avatar = models.ImageField(
        '头像',
        blank=True,
        null=True,
        upload_to=user_directory_path
    )

    #医务职称，如主任医师
    doctor_title = models.CharField(
        '医务职称',
        max_length=3,
        choices=DoctorTitle.choices,
        default=DoctorTitle.ATTENDING_PHYSICIAN
    )
    #教学职称，如教授
    teacher_title = models.CharField(
        '教学职称',
        max_length=3,
        choices=TeacherTitle.choices,
        blank=True,
        null=True
    )
    
    #医务职位, 如副院长
    doctor_office = models.CharField('医务职位', max_length=20, blank=True, null=True)
    #教学职位，如博导
    teacher_office = models.CharField(
        '教学职位',
        max_length=20,
        choices=TeacherOffice.choices,
        blank=True,
        null=True)
    #学历
    degree = models.CharField(
        '学历',
        max_length=10,
        choices=Degree.choices,
        blank=True,
        null=True
    )

    link = models.URLField('挂号网址', blank=True, max_length=300, null=True)      

    def __str__(self):
        return self.name
    
    class Meta(object):
        verbose_name = '专家库'
        verbose_name_plural = verbose_name


class Section(models.Model):
    id = models.AutoField
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

    unique_together = ('section', 'doctor')

    class Meta(object):
        verbose_name = '专业专家'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return "{} - {}".format(self.section.name, self.doctor.name)