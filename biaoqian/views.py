from django.shortcuts import render,render_to_response
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django import forms
from django.forms.models import model_to_dict

from .models import *
from django.core import serializers
import  json

# Create your views here.

def create_label(request):
    return render(request,'create_label.html')

def label_repertory(request):
    return render(request,'label_repertort.html')

def create_people(request):
    return render(request,'create_people.html')

def people_scene(request):
    return render(request,'people_scene.html')