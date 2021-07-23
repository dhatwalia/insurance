from allauthdemo.auth.insurance import Health
from allauthdemo.auth.rates import HealthRates
from allauthdemo.forms import HealthForm
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
def health(request, pk):
    health = Health.objects.get(pk = pk)
    return render(request, 'member/detail.html', {'insurance': health})

@login_required
def get_health_rates(request, instance):
    if request.method == 'POST':
        # Load the data
        data = read_csv("insurance.csv")

        # One-hot encoding
        data = get_dummies(data, columns=['sex', 'smoker', 'region'], drop_first=True)

        # Format and Split the data
        x = data[['age', 'bmi', 'children', 'sex_male', 'smoker_yes', 'region_northwest', 'region_southeast', 'region_southwest']]
        y = data['charges']
        train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.4)

        model = Sequential()
        model.add(Dense(8, input_dim=8, kernel_initializer='normal', activation='linear'))
        model.add(Dense(16, activation='linear'))
        model.add(Dense(32, activation='linear'))
        model.add(Dense(64, activation='linear'))
        model.add(Dense(32, activation='linear'))
        model.add(Dense(16, activation='linear'))
        model.add(Dense(8, activation='linear'))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mae', optimizer='adam', metrics=['mae'])
        model.fit(train_x, train_y, epochs=40, verbose=0)
        test_x = np.asarray([[instance.age, instance.bmi, instance.children, instance.sex=='male', instance.smoker=='yes', instance.region=='northwest', instance.region=='southeast', instance.region=='southwest']])
        predicted = model.predict(test_x)

        policies = HealthRates.objects.all()
        for i in range(len(policies)):
            policies[i].premium = predicted[0][0] * policies[i].premium / 12.0

    return render(request, 'forms/policies.html', {'policies': policies})

@login_required
def get_health(request, pk):
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = pk
            instance.save()
            return get_health_rates(request, instance)
    else:
        form = HealthForm()

    return render(request, 'forms/index.html', {'form': form})