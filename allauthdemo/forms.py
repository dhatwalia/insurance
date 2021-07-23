from allauthdemo.auth.insurance import *
from allauthdemo.auth.rates import *
from django import forms

class AutomotiveForm(forms.ModelForm):
    class Meta:
        model = Automotive
        exclude = ('customer_id', 'company', 'start', 'end', 'monthly_premium')

class DisabilityForm(forms.ModelForm):
    class Meta:
        model = Disability
        exclude = ('customer_id', 'start', 'end', 'monthly_premium')

class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        exclude = ('customer_id', 'start', 'end', 'monthly_premium')

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ('customer_id', 'start', 'end', 'monthly_premium')

class LifeForm(forms.ModelForm):
    class Meta:
        model = Life
        exclude = ('customer_id', 'whole', 'universal', 'annual_renewable', 'fixed_traditional', 'fixed_reentry', 'decreasing_level', 'decreasing_mortgage', 'start', 'end', 'next_premium')
