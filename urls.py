from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangovms.views.home', name='home'),
    # url(r'^djangovms/', include('djangovms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^schedule/$', 'djangovms.schedule.views.ScheduleAll'),
    url(r'^fleet/$', 'djangovms.fleet.views.AircraftAll'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
