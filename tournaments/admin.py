from django.contrib import admin

from .models import Region, County, Club, Round, Series, Tournament, Venue


admin.site.register(Region)
admin.site.register(County)
admin.site.register(Club)
admin.site.register(Round)
admin.site.register(Series)
admin.site.register(Tournament)
admin.site.register(Venue)
