from django.db import models
#Tables for Schedule

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
    )

FLIGHT_TYPES = (
    (0, 'Passenger Flight'),
    (1, 'Cargo Flight'),
    (2, 'Charter Flight'),
    )

class Schedule(models.Model):
    id = models.AutoField("ID", primary_key=True, editable=False,)
    flightnumber = models.CharField("Flight Number", max_length=6, help_text="Example: AAA134 or AAA156A")
    departureairport = models.CharField("Depature Airport", max_length=4, help_text="Example: CYYZ or EGLL")
    arrivalairport = models.CharField("Arrival Airport", max_length=4, help_text="Example: KLGA org KEWR")
    depaturetime = models.CharField("Depature Time", max_length=5, help_text="To be done in the 24 hour clock, Example: 23:31")
    arrivaltime = models.CharField("Arrival Time", max_length=5, help_text="To be done in the 24 hour clock, Example: 05:50")
    days = models.CharField(max_length=1, choices=DAYS_OF_WEEK, help_text="Drop downs :D")
    ######DISTANCE WILL GO HERE#####
    flighttype = models.CharField("Flight Type", max_length=1, choices=FLIGHT_TYPES, help_text="Drop downs :D")
    flightlevel = models.CharField("Flight Level", max_length=6, help_text="Example: 27000, needs to be done without FL")
    ticketprice = models.CharField("Ticket Price", max_length=6, help_text="Based on the currency set in settings")
    pilotforflightpay = models.CharField("Pay for Flight", max_length=5, help_text="Based on the currency set in settings")
    routedescription = models.TextField("Route Description", blank=True, max_length=3000, help_text="Notes for the route if needed")
    enabled = models.BooleanField("Active", default=False)
