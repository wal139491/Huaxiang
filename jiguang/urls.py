from django.urls import path
from django.conf.urls import url
from jiguang import views
from django.contrib import admin

urlpatterns = [
    url(r'^tuisong', views.tuisong,name='tuisong'),
    url(r'^ABtest', views.ab_test,name='abtest')
    ]