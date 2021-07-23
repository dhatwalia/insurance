from allauthdemo.auth.insurance import *
from allauthdemo.auth.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from keras.models import Sequential
from keras.layers import Dense
from pandas import *
from sklearn.model_selection import train_test_split
import numpy as np

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

