from allauthdemo.auth.insurance import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauthdemo.auth.insurance import Automotive, Disability, Health, House, Life

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
