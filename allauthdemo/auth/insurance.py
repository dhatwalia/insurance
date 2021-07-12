import datetime
from django.db import models

class Automotive(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(default=0)

    make = models.CharField(max_length=25, default='Toyota')
    model = models.CharField(max_length=100, default='Corolla')
    year = models.IntegerField(default=2010)
    abs = models.BooleanField(default=False)
    anti_theft = models.BooleanField(default=False)
    experience = models.IntegerField(default=0)

    # Coverage
    third_party = models.FloatField(default=200000)
    statutory_accident = models.FloatField(default=65000)
    uninsured_auto = models.FloatField(default=200000)
    income_replacement = models.FloatField(default=0)
    medical = models.FloatField(default=0)
    caregiver = models.FloatField(default=0)
    housekeeping = models.FloatField(default=0)
    death = models.FloatField(default=0)
    dependent = models.FloatField(default=0)
    indexation = models.FloatField(default=0)
    specified_perils = models.FloatField(default=0)
    comprehensive = models.FloatField(default=0)
    collision = models.FloatField(default=0)
    all_perils = models.FloatField(default=0)

    # Contract
    company = models.CharField(max_length=25, default='The Co-operators')
    start = models.DateField(default=datetime.date.today)
    end = models.DateField(default=datetime.date.today)
    monthly_premium = models.FloatField(default=150)

    class Meta:
        verbose_name = ('automotive')

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Automotive._meta.fields]

class Disability(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(default=0)

    # Factors
    coverage = models.FloatField(default=35000)
    benefit_period = models.IntegerField(default=1)
    waiting_period = models.IntegerField(default=0)
    age = models.IntegerField(default=40)
    health = models.IntegerField(default=10)
    occupation = models.CharField(max_length=1, default='B')

    # Contract
    start = models.DateField(default=datetime.date.today)
    end = models.DateField(default=datetime.date.today)
    monthly_premium = models.FloatField(default=100)

    class Meta:
        verbose_name = ('disability')

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Disability._meta.fields]

class Health(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(default=0)

    # Factors
    age = models.IntegerField(default=40)
    sex = models.CharField(max_length=2,default='M')
    bmi = models.FloatField(default=20.0)
    children = models.IntegerField(default=2)
    smoker = models.BooleanField(default=False)
    region = models.TextField(max_length=10, default='southeast')

    # Contract
    start = models.DateField(default=datetime.date.today)
    end = models.DateField(default=datetime.date.today)
    monthly_premium = models.FloatField(default=150)

    class Meta:
        verbose_name = ('health')

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Health._meta.fields]

class House(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(default=0)

    # Coverage
    dwelling = models.FloatField(default=10000)
    contents = models.FloatField(default=10000)
    personal_liability = models.FloatField(default=10000)
    flood = models.FloatField(blank=True, null=True)
    windstorm = models.FloatField(blank=True, null=True)
    sewer_backup = models.FloatField(blank=True, null=True)
    scheduled_articles = models.FloatField(blank=True, null=True)
    equipment_breakdown = models.FloatField(blank=True, null=True)
    guaranteed_replacement = models.FloatField(blank=True, null=True)
    earthquake = models.FloatField(blank=True, null=True)

    # Contract
    start = models.DateField(default=datetime.date.today)
    end = models.DateField(default=datetime.date.today)
    monthly_premium = models.FloatField(default=100)

    class Meta:
        verbose_name = ('house')

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in House._meta.fields]

class Life(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(default=0)

    # Coverage
    coverage = models.FloatField(default=10000)

    # Types
    whole = models.BooleanField(default=False)
    universal = models.BooleanField(default=False)
    annual_renewable = models.BooleanField(default=False)
    fixed_traditional = models.BooleanField(default=False)
    fixed_reentry = models.BooleanField(default=False)
    decreasing_level = models.BooleanField(default=False)
    decreasing_mortgage = models.BooleanField(default=False)

    # Contract
    start = models.DateField(default=datetime.date.today)
    end = models.DateField(default=datetime.date.today)
    next_premium = models.FloatField(default=1000)

    class Meta:
        verbose_name = ('life')

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in Life._meta.fields]
