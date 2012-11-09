# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from testsite.tost.views import first
from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^first/', first),    
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/filebrowser/', include(site.urls)),	
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^testsite/', include('testsite.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
