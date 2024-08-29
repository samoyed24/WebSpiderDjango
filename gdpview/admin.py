from django.contrib import admin

from .models import *


class GDPAdmin(admin.ModelAdmin):
    list_display = ('region_name', 'year', 'value')


class NationalAdmin(admin.ModelAdmin):
    list_display = ('type', 'year', 'value')


# Register your models here.
admin.site.register(GDPdata, GDPAdmin)
admin.site.register(NationalData, NationalAdmin)
