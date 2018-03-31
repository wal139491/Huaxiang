from django.urls import path
from django.conf.urls import url
from biaoqian import views
from django.contrib import admin

urlpatterns = [
    url(r'^create_label', views.create_label),
    url(r'^label_repertory', views.label_repertory),
    url(r'^create_people', views.create_people),
    url(r'^people_scene', views.people_scene),
]