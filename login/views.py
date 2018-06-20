# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.http import JsonResponse
from .models import *
import json
import  time,datetime
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

def signin(request):
    if request.POST:
        # 获取表单信息
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = Admin_user.objects.filter(email=email,password=password).values('uname','position')
        if (len(userResult) > 0):
            for i in userResult:
                print(i)
                print(type(i))
                return render(request, 'index.html',{'info':i})
        else:
            return render(request, 'login.html', {'state': "用户名或密码错误"})
    else:
        logger.error('请求错误')
        return render(request, 'login.html', {'state': "请登陆"})
          #<strong>{{ state }}</strong>  那边这样接受 应该也可以传dict


def register(request):
    if request.POST:
        name =  request.POST.get('name')
        email = request.POST.get('email')
        # pdb.set_trace()
        filterResult = Admin_user.objects.filter(email=email,name=name)
        if len(filterResult) > 0:
            return render(request, 'login.html', {"state": "用户已存在"})
        else:
            password = request.POST.get('password')
            phone = request.POST.get('password')
            dept_form = request.POST.get('dept')
            if dept_form == 1:
                dept = '大数据部'
            elif dept_form == 2:
                dept= '策略模型部'
            elif dept_form == 3:
                dept = '运营部门'
            elif dept_form == 4:
                dept = 'BI智能分析部'
            elif dept_form == 5:
                dept = '反作弊部'
            else:
                dept = '其他'
            position = request.POST.get('position')
            # 将表单写入数据库
            user = Admin_user.objects.create(name=name,email=email,password=password,phone=phone,
                                             dept=dept,position=position)
            user.save()
            return render(request, 'login.html', {'state', '注册成功'})
    else:
        return render(request,"login.html",{'state':'请注册'})

def apply(request):
    return render(request, 'apply_auth.html')

def signup(request):
    return render(request, 'register.html')

def approve(request):
    return render(request, 'approve_auth.html')


def baobiao(request):
    return render(request, 'baobiao.html')

def error404(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')

def core_data(request):
    return render(request, 'core_data.html')

def calendar(request):
    return render(request, 'calendar.html')

def mail_compose(request):
    return render(request, 'mail_compose.html')

def mailbox(request):
    return render(request, 'mailbox.html')

def get_auth(request):
    logger.error('执行')
    #user_name = request.user.name
    #  获取当前登录的用户
    user_name = '周星'
    logger.error(user_name)
    logger.error(request.POST)
    apply_theme = request.POST['zhuti']
    apply_gongneng = request.POST['gongneng']
    logger.error(apply_gongneng)
    apply_reason = request.POST.get('reason')
    logger.error(apply_reason)
    admin_name = request.POST.get('guanli')
    print(admin_name)
    dept = request.POST.get('dept')
    apply_au = apply_auth.objects.create(user_name=user_name,admin_name=admin_name, create_time=datetime.datetime.now(),
                                         apply_reason=apply_reason, apply_theme=apply_theme,
                                         dept=dept, apply_gongneng=apply_gongneng)
    apply_au.save()
    return HttpResponse('yes')



