import datetime
from django.db import models

class AutomotiveRates(models.Model):
    company = models.CharField(max_length=25, default='The Co-operators')
    
    make = models.CharField(max_length=25, default='Toyota')
    model = models.CharField(max_length=100, default='Corolla')
    year = models.IntegerField(default=2010)
    abs = models.BooleanField(default=False)
    anti_theft = models.BooleanField(default=False)
    experience = models.IntegerField(default=0)

    coverage = models.FloatField(default=200000)
    
    period = models.IntegerField(default=12)
    premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('rates_auto')

class DisabilityRates(models.Model):
    coverage = models.FloatField(default=200000)
    company = models.CharField(max_length=25, default='AllState')
    period = models.IntegerField(default=12)
    premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('rates_disability')

class HealthRates(models.Model):
    company = models.CharField(max_length=25, default='AllState')
    period = models.IntegerField(default=12)
    premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('rates_health')

class HouseRates(models.Model):
    coverage = models.FloatField(default=200000)
    company = models.CharField(max_length=25, default='AllState')
    period = models.IntegerField(default=12)
    premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('rates_house')

class LifeRates(models.Model):
    coverage = models.FloatField(default=200000)
    company = models.CharField(max_length=25, default='AllState')
    period = models.IntegerField(default=12)
    premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('rates_life')
