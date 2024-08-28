from django.db import models


class GDPdata(models.Model):
    region_name = models.TextField(null=False, blank=False)
    year = models.TextField(null=False, blank=False)
    value = models.FloatField(null=True, blank=True)
    type = models.TextField(null=False, blank=False)
