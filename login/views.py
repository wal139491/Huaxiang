# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from .models import Admin_user
# from .models import User
import pdb
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    logger.error('Something went wrong!')
    return render(request, 'index.html')
def kanban(request):
    logger.error('Something went wrong!')
    return render(request,'basic_gallery.html')

def create_label(request):
    logger.error('Something  aaa!')
    return render(request, 'article.html')

def login(request):
    logger.error('Something went wrong!')
    return render(request,'login.html', {'state': "登陆"})

def singin(request):
    if request.POST:
        # 获取表单信息
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = Admin_user.objects.filter(email=email,password=password)
        if (len(userResult) > 0):
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'state': "用户名或密码错误"})
    else:
        logger.error('不对劲')
        return render(request, 'login.html', {'state': "请登陆"})
          #<strong>{{ state }}</strong>  那边这样接受 应该也可以传dict


def register(request):
    if request.POST:
        email = request.POST.get('email')
        # pdb.set_trace()
        filterResult = Admin_user.objects.filter(email=email)
        if len(filterResult) > 0:
            return render(request, 'login.html', {"state": "用户已存在"})
        else:
            password = request.POST.get('password')
            uname = request.POST.get('uname')
            # 将表单写入数据库
            user = Admin_user.objects.create(uname=uname, password=password)
            return render(request, 'login.html', {'state', '注册成功'})
    else:
        return render(request,"login.html",{'state':'请注册'})

def apply(request):
    return render(request, 'apply_auth.html')

def approve(request):
    return render(request, 'approve_auth.html')

def yonghu360(request):
    return render(request, 'yonghu360.html')

def baobiao(request):
    return render(request, 'baobiao.html')