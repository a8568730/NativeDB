from django.conf.urls import patterns, include, url

from django.contrib import admin 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hai2gua7.views.home', name='home'),
	url(r'^', include('海外頁面.網址')),

#     url(r'^admin/', include(admin.site.urls)),
)