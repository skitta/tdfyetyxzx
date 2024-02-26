from django.contrib import admin

from .models import Doctor, OutpatientSchedule


admin.site.site_title = '微信云服务'
admin.site.site_header = '微信云服务管理后台'

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    def all_schedule(self, obj:Doctor):
        return [a.__str__() for a in obj.schedule.all()]
    
    all_schedule.short_description = '门诊排班'

    list_display = ('name', 'doctor_title', 'all_schedule')


@admin.register(OutpatientSchedule)
class OutpatientScheduleAdmin(admin.ModelAdmin):
    list_display = ('category', 'week')
