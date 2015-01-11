from django.conf.urls import patterns, include, url
#from django.contrib import admin

#adding static in development
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = patterns('',
    #own apps
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.users.urls')),
    url(r'^', include('apps.characters.urls')),
    url(r'^', include('apps.inventory.urls')),
    url(r'^', include('apps.universe.urls')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

