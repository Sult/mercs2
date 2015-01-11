from django.conf.urls import patterns, url

from apps.characters import views

urlpatterns = patterns('',
    #base character
    url(r'^character/create/$', views.create_character, name='create_character'),
    url(r'^character/$', views.character, name='character'),
    
)

