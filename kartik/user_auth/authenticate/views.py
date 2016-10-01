#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests

@csrf_exempt
def login(request):
	c={}
	c.update(csrf(request))
	return render(request,'login.html',csrf_token=c)