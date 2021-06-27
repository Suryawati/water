from django.contrib import admin
from water.models import AirValve

class AirValveAdmin(admin.ModelAdmin):
    pass
admin.site.register(AirValve, AirValveAdmin)
