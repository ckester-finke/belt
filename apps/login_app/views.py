# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
def sessCheck(request):
    try:
        return request.session['user_id']
    except:
        return False
def index(request):
    return render(request, 'login_app/index.html')
def register(request):
    results = User.objects.regVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    user = User.objects.creator(request.POST)
    messages.success(request, 'User has been created. please log in to continue')
    return redirect('/')
def login(request):
    results = User.objects.logVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    request.session['user_id'] = results['user'].id
    request.session['user_name'] = results['user'].name
    return redirect('/home')
def home(request):
    if sessCheck(request) == False:
        return redirect('/')
    return render(request, 'login_app/home.html')
def logout(request):
    request.session.flush()
    return redirect('/')