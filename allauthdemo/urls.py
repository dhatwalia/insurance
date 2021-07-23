"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
  1. Import the include() function: from django.conf.urls import url, include
  2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from .auth.views import account_profile
from .views.index import *
from .views.automotive import *
from .views.disability import *
from .views.health import *
from .views.house import *
from .views.life import *

urlpatterns = [
    # Landing page area
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),

    # Account management by allauth
    url(r'^accounts/', include('allauth.urls')),

    # Account profile and member info
    url(r'^accounts/profile/$', account_profile, name='account_profile'),
    url(r'^member/$', member_index, name='user_home'),
    url(r'^insurance/$', insurance, name='insurance'),
    
    url(r'^insurance/automotive/(?P<pk>\d+)/$', automotive, name='automotive'),
    url(r'^insurance/disability/(?P<pk>\d+)/$', disability, name='disability'),
    url(r'^insurance/health/(?P<pk>\d+)/$', health, name='health'),
    url(r'^insurance/house/(?P<pk>\d+)/$', house, name='house'),
    url(r'^insurance/life/(?P<pk>\d+)/$', life, name='life'),

    url(r'^insurance/new-automotive/(?P<pk>\d+)/$', get_automotive, name='get-automotive'),
    url(r'^insurance/new-automotive/(?P<pk>\d+)/policies/$', get_automotive_rates, name='automotive-rates'),
    url(r'^insurance/new-disability/(?P<pk>\d+)/$', get_disability, name='get-disability'),
    url(r'^insurance/new-health/(?P<pk>\d+)/$', get_health, name='get-health'),
    url(r'^insurance/new-house/(?P<pk>\d+)/$', get_house, name='get-house'),
    url(r'^insurance/new-life/(?P<pk>\d+)/$', get_life, name='get-life'),

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
