from django.conf.urls import patterns, url
from 海外頁面.介面 import 首頁
from 海外頁面.介面 import 細節描述頁
from 海外頁面.介面 import 主頁
from 海外頁面.介面 import 加語言表表格
from 海外頁面.介面 import 語言表全部json
from 海外頁面.介面 import 加類型表表格
from 海外頁面.介面 import 類型表全部json
from 海外頁面.介面 import 加原始語料表表格
from 海外頁面.介面 import 顯示全部語料



urlpatterns = patterns('',
	url(r'^index$', 主頁, name='主頁'),
	url(r'^details$', 細節描述頁, name='細節描述頁'),
	
	url(r'^加語言表表格$',加語言表表格, name='加語言表表格'),
	url(r'^語言表全部json$',語言表全部json, name='語言表全部json'),

	url(r'^加類型表表格$',加類型表表格, name='加類型表表格'),
	url(r'^類型表全部json$',類型表全部json, name='類型表全部json'),

	url(r'^加原始語料表表格$',加原始語料表表格, name='加原始語料表表格'),
# 	為了details.html顯示語料描述
	url(r'^顯示全部語料/(?P<想看的語言>[^/]*)/*$',顯示全部語料, name='顯示全部語料'),
	url(r'^顯示全部語料/(?P<想看的語言>.*)/(?P<想看的類型>[^/]*)/*$',顯示全部語料, name='顯示全部語料'),

	url(r'^.*$', 首頁, name='首頁')
)