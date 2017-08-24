from django.conf.urls import url
from django.contrib import admin
from . import views

def test(request):
    print "we here"
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
]