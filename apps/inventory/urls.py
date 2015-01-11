from django.conf.urls import patterns, url

from apps.inventory import views

urlpatterns = patterns('',
    #base character
    url(r'^hangar/$', views.hangar, name='hangar'),
    url(r'^hangar/actions/$', views.hangar_actions, name='hangar_actions'),
    url(r'^hangar/activate/(?P<pk>[0-9]+)/$', views.activate_ship, name='activate_ship'),
    
    url(r'^fitting/$', views.fitting, name='fitting'),
    url(r'^fitting/activate/(?P<pk>[0-9]+)/$', views.activate_weapon, name='activate_weapon'),
    url(r'^fitting/deactivate/(?P<pk>[0-9]+)/$', views.deactivate_weapon, name='deactivate_weapon'),
    url(r'^fitting/actions/$', views.fitting_actions, name='fitting_actions'),
)

