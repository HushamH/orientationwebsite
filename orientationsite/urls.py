"""orientationsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'orientationsite.views.home', name='home'),
    url(r'^info/$', 'orientationsite.views.info', name='info'),
    url(r'^schedule/$', 'orientationsite.views.schedule', name='schedule'),
    url(r'^team/$', 'orientationsite.views.team', name='team'),
    url(r'^media/$', 'orientationsite.views.media', name='media'),
    url(r'^contact/$', 'orientationsite.views.contact', name='contact'),
    url(r'^register/$', 'orientationsite.views.register', name='register'),
    url(r'^profile/$', 'orientationsite.apps.registrationmanager.views.profile', name='profile'),
    url(r'^regform/$', 'orientationsite.views.regform', name='regform'),
    url(r'^checkout/$', 'orientationsite.apps.checkout.views.checkout', name='checkout'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',views.home_files, name='home-files'),


]
