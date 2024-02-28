import os

from django.db import models
from django.utils.translation import gettext_lazy as _


class Profession(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta(object):
        verbose_name = '专业'
        verbose_name_plural = verbose_name


class OutpatientSchedule(models.Model):

    class Category(models.TextChoices):
        GENERAL = 'GP', _('普通专家门诊')
        SENIOR = 'SP', _('高级专家门诊')

    class Week(models.IntegerChoices):
        MONDAY = 0, _('星期一')
        TUESDAY = 1, _('星期二')
        WEDNESDAY = 2, _('星期三')
        THURSDAY = 3, _('星期四')
        FRIDAY = 4, _('星期五')
        SATURDAY = 5, _('星期六')
        SUNDAY = 6, _('星期日')

    id = models.AutoField
    category = models.CharField('门诊类别',
        max_length=2,
        choices=Category.choices,
        default=Category.GENERAL
    )
    week = models.IntegerField('班次', choices=Week.choices)

    def display(self):
        w = self.Week.choices[self.week]
        c = next((t for t in self.Category.choices if self.category in t), None)
        return '{}({})'.format(w[1], c[1])

    def __str__(self):
        return self.display()
    
    class Meta(object):
        verbose_name = '门诊排班'
        verbose_name_plural = verbose_name


class Doctor(models.Model):

    class DoctorTitle(models.TextChoices):
        ATTENDING_PHYSICIAN = 'AP', _('主任医师')
        ASSOCIATE_ATTENDING_PHYSICIAN = 'AAP', _('副主任医师')
        CHIEF_RESIDENT = 'CR', _('主治医师')

    class TeacherTitle(models.TextChoices):
        PROFESSOR = 'PR', _('教授')
        ASSOCIATE_PROFESSOR = 'APR', _('副教授')

    class Degree(models.TextChoices):
        BACHELOR_MEDICINE = 'MB', _('医学学士')
        MASTER_MEDICINE = 'MM', _('医学硕士')
        DOCTOR_MEDICINE = 'MD', _('医学博士')
    
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

    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return '/media/avatar/default.png'

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
        default=TeacherTitle.PROFESSOR,
        blank=True,
        null=True
    )
    
    #医务职位, 如副院长
    doctor_office = models.CharField('医务职位', max_length=20, blank=True, null=True)
    #教学职位，如博导
    teacher_office = models.CharField('教学职位', max_length=20, blank=True, null=True)
    #学历
    degree = models.CharField(
        '学历',
        max_length=10,
        choices=Degree.choices,
        default=Degree.DOCTOR_MEDICINE
    )
    #专业
    major = models.ManyToManyField(verbose_name='专业',to=Profession)
    #擅长
    field = models.TextField('擅长领域')
    #介绍
    info = models.TextField('介绍')
    #门诊排班
    schedule = models.ManyToManyField(verbose_name='门诊排班', to=OutpatientSchedule)
    link = models.URLField('挂号网址', blank=True)

    def __str__(self):
        return self.name
    
    class Meta(object):
        verbose_name = '专家库'
        verbose_name_plural = verbose_name
