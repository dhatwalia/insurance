from allauthdemo.auth.insurance import Automotive
from allauthdemo.auth.rates import AutomotiveRates
from allauthdemo.forms import AutomotiveForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pandas import *

@login_required
def automotive(request, pk):
    automotive = Automotive.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': automotive})

@login_required
def get_automotive_rates(request, instance):
    if request.method == 'POST':
        coverage = instance.third_party + instance.statutory_accident + instance.uninsured_auto + instance.income_replacement + instance.medical + instance.caregiver + instance.housekeeping + instance.death + instance.dependent + instance.indexation + instance.specified_perils + instance.comprehensive + instance.collision + instance.all_perils
        policies = AutomotiveRates.objects.filter(
            make = instance.make,
            model = instance.model,
            year = instance.year,
            abs = instance.abs,
            anti_theft = instance.anti_theft,
            experience = instance.experience,
            coverage = coverage,
        )
        return render(request, 'forms/policies.html', {'policies': policies})

@login_required
def get_automotive(request, pk):
    if request.method == 'POST':
        form = AutomotiveForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return get_automotive_rates(request, instance)
    else:
        form = AutomotiveForm()

    return render(request, 'forms/index.html', {'form': form})
