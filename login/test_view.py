# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.http import JsonResponse
from .models import Admin_user
import json
import time, datetime
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
# from .models import User
import pdb
import csv
import logging
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    logger.error('Something went wrong!')
    return render(request, 'index.html')


def kanban(request):
    logger.error('Something went wrong!')
    return render(request, 'basic_gallery.html')


def create_label(request):
    logger.error('Something  aaa!')
    return render(request, 'article.html')


def login(request):
    logger.error('Something went wrong!')
    return render(request, 'login.html', {'state': "登陆"})


def signin(request):
    if request.POST:
        # 获取表单信息
        email = request.POST.get('email')
        password = request.POST.get('password')
        userResult = Admin_user.objects.filter(email=email, password=password)
        if (len(userResult) > 0):
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'state': "用户名或密码错误"})
    else:
        logger.error('请求错误')
        return render(request, 'login.html', {'state': "请登陆"})
        # <strong>{{ state }}</strong>  那边这样接受 应该也可以传dict


def register(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        # pdb.set_trace()
        filterResult = Admin_user.objects.filter(email=email, name=name)
        if len(filterResult) > 0:
            return render(request, 'login.html', {"state": "用户已存在"})
        else:
            password = request.POST.get('password')
            phone = request.POST.get('password')
            dept_form = request.POST.get('dept')
            if dept_form == 1:
                dept = '大数据部'
            elif dept_form == 2:
                dept = '策略模型部'
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
            user = Admin_user.objects.create(name=name, email=email, password=password, phone=phone,
                                             dept=dept, position=position)
            user.save()
            return render(request, 'login.html', {'state', '注册成功'})
    else:
        return render(request, "login.html", {'state': '请注册'})


def apply(request):
    return render(request, 'apply_auth.html')


def signup(request):
    return render(request, 'register.html')


def approve(request):
    return render(request, 'approve_auth.html')


def yonghu360(request):
    return render(request, 'yonghu360.html')


def baobiao(request):
    return render(request, 'baobiao.html')


def error404(request):
    return render(request, '404.html')


def error500(request):
    return render(request, '500.html')


def apply_au(request):
    if request.POST:
        # 获取表单信息
        user_name = request.user.name #获取当前登录的用户
        theme = request.POST['theme']
        applylist =  request.POST['gongneng']
        reason = request.POST.get('reason')
        guanli = request.POST.get('guanli')
        dept_form = request.POST.get('dept')
        apply_au = Apply_auth.objects.create(name=user_name, date=datetime.date.today(), reason=reason, theme=theme,
                                             dept=dept, applylist=applylist)
        apply_au.save()
        return render(request, 'apply_auth.html', {'state', '申请成功'})


# 管理员管理审批记录
def approve_au(request):
    if request.POST:
        # 获取权限申请单对应该管理员的操作列表
        apply_data = Apply_auth.objects.fliter(name='赖伟', is_operate=0).values()
        # 获得了管理员赖伟未处理过的申请单元组列表供前台显示
        return render(request, 'approve_auth.html', {'apply_data', 'apply_data'})


def bohui(request):
    if request.POST:
        # 拒绝普通用户的申请单
        Apply_auth.objects.filter(apply_id=request.POST.get('apply_id')).update(is_operate=1)
        return return render(request, 'approve_auth.html', {'state', '操作成功'})

def tongguo(request):
    if request.POST:
        # 同意普通用户的申请单
        apply_list = request.POST.get('apply_list')
        for i in apply_list:
            auth_name = 'auth'+str(i)
            auth_dict = {auth_name:1}
            # 根据申请单申请的权限列表更新
            Auth_base.objects.filter(id=request.user.user_id).update(**auth_dict)
        return render(request, 'approve_auth.html', {'state', '操作成功'})


def create_label(request):
    # 如果当前用户是管理员
    if  request.POST and request.user.type == '管理员':
        label_cate = request.POST.get('label_cate')
        if label_cate == 1:
            lcategory = '基础类标签'
        elif label_cate == 2:
            lcategory = '挖掘类标签'
        label1_name = request.POST.get('label1_name')
        label2_name = request.POST.get('label2_name')
        uploaded_file = request.FILES.get["ID_Set"]
        f = csv.reader(uploaded_file,'r') #读取csv格式的用户ID集合
        id_list = []
        for id in f:
            id_list.append(id)
        label = Label_create.objects.create(name=request.user.user_name, create_time=datetime.date.today(), label_cate=lcategory, label_level1=label1_name,
                                             label_name=label2_name,user_id_set=id_list)
        label.save()
        return render(request, 'create_label.html', {'state', '创建标签成功'})


# 标签仓库查询
def label_repertory(request):
    # 如果当前用户是管理员
    if  request.GET:
        if 'category' in request.GET: # 如果查询的是标签类别
            dict_cate = {1:'基础类标签',2:'挖掘类标签'}
            result = Label_create.objects.fliter(dict_cate[request.GET['l_category']]).values()
            return render(request, 'label_repertort.html', {'data', result})
        elif 'label2' in request.GET: #如果查询的是二级标签
            level1 = Label_statistic.objects.fliter(value=request.GET['lable2'])
            result = Label_create.objects.fliter(label_level1=level1).values()
            return render(request, 'label_repertort.html', {'data', result})


def create_people(request):
    # 如果当前用户是管理员
    if  request.POST:
        people_name = request.POST.get('people_name')
        people_describe = request.POST.get('describe')
        use_for = {1: '运营推送', 2: 'AB测试', 3: '人群分析'}
        bumen = {1: '大数据部', 2: '策略模型部', 3: '运营部门', 4: 'BI智能分析部', 5: '反作弊部', 6: '其他'}
        use_type = use_for[request.POST.get('use_type')]
        dept = bumen[request.POST.get('dept')]
        renqun_list1 = request.POST.getlist('renqun_list1')
        renqun_list2 = request.POST.getlist('renqun_list2')
        list1 = Label_create.objects.filter(label_name__in = renqun_list1)  #获取人群id1集合
        list2 = Label_create.objects.filter(label_name__in=renqun_list2)
        if request.POST.get('operation')==1:
            #如果取并集
            renqun = set(list1).union(set(list2))
        else: #如果取交集
            requn = set(list1).intersection(set(list2))

        renqun = People_label.objects.create(name=request.user.user_name,people_name=people_name, create_time=datetime.date.today(),  people_describe= people_describe, dept=dept,
                                             use_type=use_type,user_id_set=renqun)
        renqun.save()
        return render(request, 'create_people.html', {'state', '创建人群成功'})


# 人群洞察先不写了
def people_scene(request):
    # 如果当前用户是管理员
    if  request.GET:
        if 'category' in request.GET: # 如果查询的是标签类别
            dict_cate = {1:'基础类标签',2:'挖掘类标签'}
            result = Label_create.objects.fliter(dict_cate[request.GET['l_category']]).values()
            return render(request, 'label_repertort.html', {'data', result})
        elif 'label2' in request.GET: #如果查询的是二级标签
            level1 = Label_statistic.objects.fliter(value=request.GET['lable2'])
            result = Label_create.objects.fliter(label_level1=level1).values()
            return render(request, 'label_repertort.html', {'data', result})


def yonghu_scene(request):
    if request.method == 'POST':
        if request.is_ajax():#接受前端的用户ID请求
            cos_id = request.POST.get('cos_id')
            data = Customer.obejcts.fliter(cos_id).values() #查询这个用户ID的属性
            my_wordcloud = WordCloud().generate(data.labels) #生成词云图片
            image = Image.open(BytesIO(my_wordcloud))
            image.save('/static/img/ciyun.png')
            return JsonResponse(data)

    return render(request, 'yonghu360.html')


def tuisong(request):
    if  request.POST:
        people_name = request.POST.get('people_name')
        send_date = request.POST.get('send_date')
        send_time = request.POST.get('send_time')
        send_text = request.POST.get('send_text')
        people_id_list = People_label.objects.fliter(people_name__in = people_name).values('user_id_set')
        mail_list = User_mail.objects.fliter(id__in = people_id_list)
        sender = 'from@auraro.com'

        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText(send_text, 'plain', 'utf-8')
        message['From'] = Header("Auraro活动", 'utf-8')
        message['Subject'] = Header("来自Auraro的问候", 'utf-8')

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, mail_list, message.as_string())
            return render(request, 'tuisong.html',{'state':'推送成功'})
        except smtplib.SMTPException:
            return render(request, 'tuisong.html', {'state': '失败'})











