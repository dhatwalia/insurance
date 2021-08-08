from allauthdemo.auth.insurance import *
from allauthdemo.auth.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
def delete(request, type, id):
    if type == 'automotive':
        item = Automotive.objects.get(id = id)
    elif type == 'disability':
        item = Disability.objects.get(id = id)
    elif type == 'health':
        item = Health.objects.get(id = id)
    elif type == 'house':
        item = House.objects.get(id = id)
    else:
        item = Life.objects.get(id = id)

    item.delete()
    return redirect('insurance')
