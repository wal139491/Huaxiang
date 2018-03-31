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

# Get an instance of a logger
logger = logging.getLogger(__name__)

def kanban1(request):

    # logger.error('加载客户端看板成功')
    # values_list 返回的就是元组，values返回的queryset
    # qu_rsult =  App_statistic.objects.all().values_list('city', flat=True).distinct()
    # #app_new = App_statistic.objects.all().values_list('city', flat=True).distinct()# filter用来过滤条件，支持in like 多用filter吧
    # app_new = json.dumps(list(qu_rsult), cls=DjangoJSONEncoder)
    # u_dict = model_to_dict(u)
    # logger.error(type(app_new))
    # logger.error('前面美执行')
    return render(request, 'graph_echarts.html')

def yunying(request):
    return render(request, 'yunying.html')

def hexing(request):
    qu_rsult = top_statistic.objects.all().values()

    dict6 = {
        {'value':qu_rsult.top1_category,'name':qu_rsult.top1_rate},
        {'value': qu_rsult.top2_category, 'name': qu_rsult.top2_rate},
        {'value': qu_rsult.top3_category, 'name': qu_rsult.top3_rate},
        {'value': qu_rsult.top4_category, 'name': qu_rsult.top4_rate},
        {'value': qu_rsult.top5_category, 'name': qu_rsult.top5_rate},
        {'value': qu_rsult.top6_category, 'name': qu_rsult.top6_rate}
    }
    return render(request, 'hexing.html',dict6)

# def app_count(request):

def kanban2(request):
	if request.method == 'GET':
		data = {'data': [
			{'value': 335, 'name': '直接访问'},
			{'value': 310, 'name': '邮件营销'},
			{'value': 234, 'name': '联盟广告'},
			{'value': 135, 'name': '视频广告'},
			{'value': 1548, 'name': '搜索引擎'}
		],
			'categories': ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']}
		return JsonResponse(data)



def aaa_test(request):
    app_sta = App_statistic.objects.all().values()  # 为什么加values,因为之前返回的是对象，values返回字典
    city = App_statistic.objects.all().distinct('city').values()  # filter用来过滤条件，支持in like 多用filter吧
    app_date = App_statistic.objects.all().distinct('dt').values()
    # app_static = App_statistic.objects.filter().values(''city','new_count')
    app_new = App_statistic.objects.filter().values('city', 'new_count')
    app_active = App_statistic.objects.filter().values('city', 'active_uconut')
    logger.error(type(app_new))
    return render(request,'aaa.html',{'app_new':app_new})

# app端新增
def app_count(request):
     app_sta = App_statistic.objects.All().values() #为什么加values,因为之前返回的是对象，values返回字典
     city = App_statistic.objects.all().distinct('city').values()  # filter用来过滤条件，支持in like 多用filter吧
     app_date = App_statistic.objects.all().distinct('dt').values()
     # app_static = App_statistic.objects.filter().values(''city','new_count')
     app_new = App_statistic.objects.filter().values('city', 'new_count')
     app_active = App_statistic.objects.filter().values('city', 'active_uconut')
     return JsonResponse(app_sta)

def quset():
    qu_rsult = App_statistic.objects.all().values_list('city', flat=True).distinct()
    return qu_rsult

