from django.conf.urls import patterns, url

from apps.universe import views

urlpatterns = patterns('',
    url(r'^travel/$', views.travel, name='travel'),
)
