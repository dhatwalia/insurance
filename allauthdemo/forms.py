from allauthdemo.auth.insurance import *
from django import forms

class AutomotiveForm(forms.ModelForm):
    class Meta:
        model = Automotive
        exclude = ('customer_id', 'start', 'end', 'monthly_premium')

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

class LifeForm(forms.Form):
    coverage = forms.FloatField()
    permanent = forms.BooleanField(label='Do you want a permanent life insurance?', required=False)
    permanent_change = forms.BooleanField(label='Do you want to change the death benefit amount or suspend the premium?', required=False)
    only_year = forms.BooleanField(label='Is it only for a year OR urgently needed?', required=False)
    less_than_10 = forms.BooleanField(label='IS it for a less than 10 year reentry period?', required=False)
    small_budget = forms.BooleanField(label='Do you have a small budget?', required=False)

    def save(self, commit):
        return
