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
from 海外頁面.介面 import index初始顯示語言
# from 海外頁面.介面 import 上傳檔案
from hai2gua7 import settings
from 海外頁面.介面 import 顯示原始語料表
from 海外頁面.介面 import 後台
from 海外頁面.介面揣語料檔案 import 揣著語料的全部檔案
from 海外頁面.介面揣語料檔案 import 顯示xlsx的音
from 海外頁面.介面揣語料檔案 import 刪除一個檔案
from 海外頁面.介面揣語料檔案 import 語料的全部檔案json
from 海外頁面.介面揣語料檔案 import 測試批次刪除
from 海外頁面.介面揣語料檔案 import 測試抓網址
from 海外頁面.介面揣語料檔案 import 顯示合格的EXCEL與字格
from 海外頁面.介面揣語料檔案 import 刪除轉好的表
from 海外頁面.介面前臺 import 顯示語言漢字相同的音檔



urlpatterns = patterns('',
	url(r'^index$', 主頁, name='主頁'),
	url(r'^details$', 細節描述頁, name='細節描述頁'),
	url(r'^後台$', 後台, name='後台'),
	
	url(r'^加語言表表格$',加語言表表格, name='加語言表表格'),
	url(r'^語言表全部json$',語言表全部json, name='語言表全部json'),

	url(r'^加類型表表格$',加類型表表格, name='加類型表表格'),
	url(r'^類型表全部json$',類型表全部json, name='類型表全部json'),

	url(r'^加原始語料表表格$',加原始語料表表格, name='加原始語料表表格'),
# 	為了details.html顯示語料描述
	url(r'^顯示全部語料/(?P<想看的語言>[^/]*)/*$',顯示全部語料, name='顯示全部語料'),
	url(r'^顯示全部語料/(?P<想看的語言>.*)/(?P<想看的類型>[^/]*)/*$',顯示全部語料, name='顯示全部語料'),

	url(r'^index$',index初始顯示語言, name='index初始顯示語言'),
	url(r'^index/*$',index初始顯示語言, name='index初始顯示語言'),
	url(r'^index/(?P<想看的語言>[^/]+)/*$',index初始顯示語言, name='index初始顯示語言'),
	
# 	url(r'^上傳檔案$', 上傳檔案, name='上傳檔案'),
	url(r'^顯示原始語料表$', 顯示原始語料表, name='顯示原始語料表'),
	url(r'^(?P<語料編號>\d+)/揣著語料的全部檔案$', 揣著語料的全部檔案, name='揣著語料的全部檔案'),
	
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
	url(r'^顯示xlsx的音/(?P<xlsx檔名>[^/]+)/(?P<字數>[^/]+)/*$', 顯示xlsx的音, name='顯示xlsx的音'),
	
	url('^(?P<檔案編號>\d+)/刪除一個檔案$', 刪除一個檔案, name='刪除一個檔案'),
	
	url('^(?P<語料編號>\d+)/測試批次刪除$', 測試批次刪除, name='測試批次刪除'),
	
	url('^測試抓網址/(?P<語料編號>[^/]+)/*$', 測試抓網址, name='測試抓網址'),
	
	url('^(?P<語料編號>\d+)/顯示合格的EXCEL與字格$', 顯示合格的EXCEL與字格, name='顯示合格的EXCEL與字格'),
	
	url('^語料的全部檔案json$', 語料的全部檔案json, name='語料的全部檔案json'),
	
	url('^(?P<語料編號>\d+)/刪除轉好的表$', 刪除轉好的表, name='刪除轉好的表'),
	
	url('^(?P<語言名稱>[^/]+)/顯示語言漢字相同的音檔$', 顯示語言漢字相同的音檔, name='顯示語言漢字相同的音檔'), 
	
	url(r'^.*$', 首頁, name='首頁')
)


# 可以下載檔案
# if settings.DEBUG:
#     urlpatterns = patterns('',
#         
# )