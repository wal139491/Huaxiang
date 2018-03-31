from django.urls import path
from django.conf.urls import url
from kanban import views
from django.contrib import admin

urlpatterns = [
    url(r'^graph_echarts', views.kanban1,name='kanban1'),
    url(r'^aaa',views.aaa_test),
    url(r'^yunying',views.yunying),
    url(r'^hexing',views.hexing),
    ]