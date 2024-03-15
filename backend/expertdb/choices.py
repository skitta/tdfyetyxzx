from django.db import models
from django.utils.translation import gettext_lazy as _


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