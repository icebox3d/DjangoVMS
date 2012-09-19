from django.db import models
#Tables for Aircraft
class Aircraft(models.Model):
    id = models.AutoField("ID", primary_key=True, editable=False)
    icao = models.CharField("ICAO", max_length=6)
    type = models.CharField("Full Name", max_length=30)
    reg = models.CharField("Registration", max_length=20)
    maxpax = models.CharField("Maximum Passengers", max_length=6)
    maxcargo = models.CharField("Maximum Cargo", max_length=10)
    maxrange = models.CharField("Maximum Range", max_length=10)
    maxweight = models.CharField("Maximum Weight", max_length=10)
    maxcruise = models.CharField("Maximum Cruise", max_length=10)
    aircraftdl = models.URLField("Aircraft Download Link", blank = False)
    aircraftimage = models.URLField("Aircraft Image", blank = False)
