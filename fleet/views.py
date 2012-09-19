from django.shortcuts import render_to_response
from django.template import RequestContext
from djangovms.fleet.models import Aircraft



def AircraftAll(request):
    aircraftcount = Aircraft.objects.count()
    pagetitle = 'All Servers'
    aircrafts = Aircraft.objects.all()
    context = {'aircrafts': aircrafts, 'aircraftcount': aircraftcount, 'pagetitle': pagetitle}
    return render_to_response('fleet.html', context, context_instance=RequestContext(request))