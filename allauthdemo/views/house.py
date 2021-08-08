from allauthdemo.auth.insurance import House
from allauthdemo.auth.rates import HouseRates
from allauthdemo.forms import HouseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pandas import *

@login_required
def house(request, pk):
    house = House.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': house, 'type': 'house'})

@login_required
def get_house_rates(request, instance):
    if request.method == 'POST':
        coverage = instance.dwelling + instance.contents + instance.personal_liability + instance.flood + instance.windstorm + instance.sewer_backup + instance.scheduled_articles +instance.equipment_breakdown + instance.guaranteed_replacement + instance.earthquake
        policies = HouseRates.objects.filter(
            coverage = coverage,
        )
        return render(request, 'forms/policies.html', {'policies': policies})

@login_required
def get_house(request, pk):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return get_house_rates(request, instance)
    else:
        form = HouseForm()

    return render(request, 'forms/index.html', {'form': form})
    