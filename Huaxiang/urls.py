"""Huaxiang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), #管理员
    url(r'^index', views.index),
    url(r'^login',views.signin),
    url(r'^register',views.signup),
    url(r'^apply_auth',views.apply),
    url(r'^approve_auth',views.approve),
    url(r'^core_data', views.core_data),
    url(r'^baobiao', views.baobiao),
    url(r'^404error', views.error404),
    url(r'^500error', views.error500),
    # url(r'^$', views.signin)
    url(r'^register',views.register),
    url(r'^get_auth',views.get_auth),
    url(r'^calendar',views.calendar),
    url(r'^mailbox',views.mailbox),
    url(r'^mail_compose',views.mail_compose),
    # 看板模块
    url('^jiguang/',include('jiguang.urls')),
    url('^kanban/',include('kanban.urls')), # 包含看板APP的urls
    url('^biaoqian/',include('biaoqian.urls')) # 包含看板APP的urls

]
