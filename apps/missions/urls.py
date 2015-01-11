from django.conf.urls import patterns, url

from apps.missions import views

urlpatterns = patterns('',
    #base character
    url(r'^bounties/$', views.bounties, name='bounties'),
)

