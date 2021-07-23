from allauthdemo.auth.insurance import Life
from allauthdemo.auth.rates import LifeRates
from allauthdemo.forms import LifeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pandas import *

@login_required
def life(request, pk):
    life = Life.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': life})

@login_required
def get_life_rates(request, instance):
    if request.method == 'POST':
        policies = LifeRates.objects.filter(
            coverage = instance.coverage,
        )
        return render(request, 'forms/policies.html', {'policies': policies})

@login_required
def get_life(request, pk):
    if request.method == 'POST':
        form = LifeForm(request.POST)
        if form.is_valid():
            permanent_need = form.cleaned_data['permanent_need']
            permanent_change = form.cleaned_data['permanent_need_but_can_be_changed']
            only_for_a_year = form.cleaned_data['only_for_a_year']
            less_than_10 = form.cleaned_data['less_than_10']
            small_budget = form.cleaned_data['small_budget']
            
            instance = form.save(commit=False)
            instance.customer_id = pk
            if permanent_need:
                if permanent_change:
                    instance.universal = True
                else:
                    instance.whole = True
            else:
                if only_for_a_year:
                    if less_than_10:
                        instance.annual_renewable = True
                    else:
                        if small_budget:
                            instance.fixed_reentry = True
                        else:
                            instance.fixed_traditional = True  
            instance.save()
            return get_life_rates(request, instance)
    else:
        form = LifeForm()

    return render(request, 'forms/index.html', {'form': form})
