"""
trip admin

"""
from django.contrib import admin
from ctrip.models import Departure, Trip



class DepartureInline(admin.StackedInline):
    """
    departure inline admin
    """

    model = Departure
    extra = 0


class TripAdmin(admin.ModelAdmin):
    """
    trip admin
    """
    prepopulated_fields = {'slug': ('name', )}

    inlines = [
        DepartureInline,
    ]

admin.site.register(Trip, TripAdmin)
