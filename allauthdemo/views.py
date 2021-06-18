from allauthdemo.auth.insurance import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def member_index(request):
    t = loader.get_template('member/index.html')
    c = {}
    return HttpResponse(t.render(c, request), content_type='text/html')

@login_required
def insurance(request):
    automotive = Automotive.objects.all()
    disability = Disability.objects.all()
    health = Health.objects.all()
    house = House.objects.all()
    life = Life.objects.all()

    return render(request, 'member/insurance.html',{
        'automotive': automotive,
        'disability': disability,
        'health': health,
        'house': house,
        'life': life,
    })

@login_required
def automotive(request, pk):
    automotive = Automotive.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': automotive})

@login_required
def disability(request, pk):
    disability = Disability.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': disability})

@login_required
def health(request, pk):
    health = Health.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': health})

@login_required
def house(request, pk):
    house = House.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': house})

@login_required
def life(request, pk):
    life = Life.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': life})

@login_required
def get_automotive(request, pk):
    if request.method == 'POST':
        form = AutomotiveForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return HttpResponse('Response submitted')
    else:
        form = AutomotiveForm()

    return render(request, 'forms/index.html', {'form': form})

@login_required
def get_disability(request, pk):
    if request.method == 'POST':
        form = DisabilityForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return HttpResponse('Response submitted')
    else:
        form = DisabilityForm()

    return render(request, 'forms/index.html', {'form': form})

@login_required
def get_health(request, pk):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return HttpResponse('Response submitted')
    else:
        form = HealthForm()

    return render(request, 'forms/index.html', {'form': form})

@login_required
def get_house(request, pk):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return HttpResponse('Response submitted')
    else:
        form = HouseForm()

    return render(request, 'forms/index.html', {'form': form})

@login_required
def get_life(request, pk):
    if request.method == 'POST':
        form = LifeForm(request.POST)
        if form.is_valid():
            permanent = form.cleaned_data['permanent']
            permanent_change = form.cleaned_data['permanent_change']
            only_year = form.cleaned_data['only_year']
            less_than_10 = form.cleaned_data['less_than_10']
            small_budget = form.cleaned_data['small_budget']

            life = Life()
            if permanent:
                if permanent_change:
                    life.universal = True
                else:
                    life.whole = True
            else:
                if only_year:
                    if less_than_10:
                        life.annual_renewable = True
                    else:
                        if small_budget:
                            life.fixed_reentry = True
                        else:
                            life.fixed_traditional = True

            life.customer_id = pk            
            life.save()
            return HttpResponse('Response submitted')
    else:
        form = LifeForm()

    return render(request, 'forms/index.html', {'form': form})
