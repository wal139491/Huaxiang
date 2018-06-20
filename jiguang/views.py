# -*- coding=utf-8 -*-
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django import forms
from django.forms.models import model_to_dict

from .models import *
from django.core import serializers
import  json
# Create your views here.

import logging


def tuisong(request):
    return render(request, 'tuisong.html')

def ab_test(request):
    return render(request, 'ABtest.html')