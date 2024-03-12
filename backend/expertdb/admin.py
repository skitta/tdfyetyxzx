from django.contrib import admin

from .models import Doctor, Section, SectionDoctors


admin.site.site_title = '微信云服务'
admin.site.site_header = '微信云服务管理后台'

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_title', 'teacher_title', 'teacher_office', 'degree')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    readonly_fields = ('doctors',)


@admin.register(SectionDoctors)
class SectionDoctorsAdmin(admin.ModelAdmin):
    list_display = ('section', 'doctor')
