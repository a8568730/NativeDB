from django.conf.urls import patterns, url
from 海外頁面.介面 import 首頁


urlpatterns = patterns('',
	url(r'^.*$', 首頁, name='首頁'),

)