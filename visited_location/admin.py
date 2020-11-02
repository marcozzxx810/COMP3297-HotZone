from django.contrib import admin
from visited_location.models import Location, VisitedLocationRecord
# Register your models here.
admin.site.register(Location)
admin.site.register(VisitedLocationRecord)