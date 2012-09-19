from djangovms.schedule.models import Schedule
from django.contrib import admin

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id']
    search_fields = ['reg']

admin.site.register(Schedule,ScheduleAdmin)