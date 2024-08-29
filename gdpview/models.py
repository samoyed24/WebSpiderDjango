from django.contrib.admin import register
from django.db import models


class GDPdata(models.Model):
    region_name = models.TextField(null=False, blank=False)
    year = models.TextField(null=False, blank=False)
    value = models.FloatField(null=True, blank=True)
    type = models.TextField(null=False, blank=False)

    # def __str__(self):
    #     return f"{self.region_name}{self.year}年GDP：{self.value}亿元"


class NationalData(models.Model):
    type = models.TextField(null=False, blank=False)
    value = models.FloatField(null=True, blank=True)
    year = models.TextField(null=False, blank=False)

    # def __str__(self):
    #     return f"我国{self.year}年{self.type}：{self.value}亿元/元"
