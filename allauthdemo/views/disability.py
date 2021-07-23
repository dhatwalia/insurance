from allauthdemo.auth.insurance import Disability
from allauthdemo.auth.rates import DisabilityRates
from allauthdemo.forms import DisabilityForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pandas import *

@login_required
def disability(request, pk):
    disability = Disability.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': disability})

@login_required
def get_disability_rates(request, instance):
    if request.method == 'POST':
        policies = DisabilityRates.objects.filter(
            coverage = instance.coverage,
        )
        return render(request, 'forms/policies.html', {'policies': policies})

@login_required
def get_disability(request, pk):
    if request.method == 'POST':
        form = DisabilityForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return get_disability_rates(request, instance)
    else:
        form = DisabilityForm()

    return render(request, 'forms/index.html', {'form': form})
