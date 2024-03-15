from django.contrib import admin
from django.utils.text import Truncator

from .models import Doctor, Section, SectionDoctors


admin.site.site_title = '微信云服务'
admin.site.site_header = '微信云服务管理后台'


class SectionDoctorsInline(admin.TabularInline):
    model = SectionDoctors
    extra = 1


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'doctor_title', 'teacher_title', 'teacher_office', 'degree', 'short_link_str')
    search_fields = ('name',)

    def short_link_str(self, obj):
        if obj.link is not None and len(obj.link) > 10:
            link_str = obj.link[:10] + '...' + obj.link[-10:]
            return link_str
        
    short_link_str.short_description = '挂号链接'


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_doctors')
    
    def display_doctors(self, obj):
        return ', '.join([doctor.name for doctor in obj.doctors.all()])
    
    display_doctors.short_description = '专家列表'
    

@admin.register(SectionDoctors)
class SectionDoctorsAdmin(admin.ModelAdmin):
    list_display = ('section', 'doctor', 'short_info')

    def short_info(self, obj):
        return Truncator(obj.info).chars(25)
    
    short_info.short_description = '简介'
