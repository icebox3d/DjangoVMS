from djangovms.fleet.models import Aircraft
from django.contrib import admin

class AircraftAdmin(admin.ModelAdmin):
    list_display = ['id', 'icao', 'type', 'reg', 'maxpax', 'maxcargo']
    search_fields = ['reg']

admin.site.register(Aircraft,AircraftAdmin)