from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic.base import View
from 海外頁面.表格 import 顯示語言表表格
from 海外頁面.模型 import 語言表
import json
from 海外頁面.表格 import 顯示類型表表格
from 海外頁面.模型 import 類型表
from 海外頁面.模型 import 原始語料表
from 海外頁面.表格 import 顯示原始語料表表格
from django.shortcuts import render_to_response
from django import forms
from 海外頁面.表格 import 上傳檔案表格
from django.core.context_processors import csrf
from django.utils.encoding import smart_str
import os.path
from hai2gua7.settings import MEDIA_ROOT
from 海外頁面.模型 import 原始檔案表
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json
from NativeDB_py.取出聲音位置 import 取出聲音位置
from NativeDB_py.檢查輸入的檔案 import 檢查輸入
from NativeDB_py.合併音節的位置 import 合併位置
from NativeDB_py.檢查取出的位置大小 import 檢查位置大小
from NativeDB_py.合併的音標比對excel import 音標比對excel
from NativeDB_py.合併音標 import 合併音標

def 首頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/first.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 主頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/index.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 細節描述頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/details.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 後台(request):
	template = loader.get_template('海外頁面/後台.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 加語言表表格(request):
	if request.method == 'POST':  # If the form has been submitted...
		# 	request.POST=['語言':'...', '類型':'...', ]->傳給表格.py的顯示語言表->傳給模型.py的語言表確認只有語言欄位。
		語言表格 = 顯示語言表表格(request.POST)  # A form bound to the POST data
		if 語言表格.is_valid():
			語言 = 語言表格.save()
			#	redirect 屬於GET方法
			return redirect('加語言表表格')
	else:
		語言表格 = 顯示語言表表格()
# 	template = loader.get_template('海外頁面/新文章.html')
# 	context = RequestContext(request, {
# 		'文章': 文章表格,
# 	})
# 	return HttpResponse(template.render(context))
	揣著語言 = 語言表.objects.all()
	# 	決定要有哪些輸入欄位
	return render(request, '海外頁面/新語言.html', {
		'語言': 語言表格,
		'揣著語言':揣著語言,
		'介面名': '加語言表表格'
	})

def 語言表全部json(request):
	全部語言=[]
	for 揣著語言 in 語言表.objects.all():
		全部語言.append(揣著語言.語言)
	return HttpResponse(json.dumps(全部語言), content_type="application/json")


def 加類型表表格(request):
	if request.method == 'POST':  # If the form has been submitted...
		類型表格 = 顯示類型表表格(request.POST)  # A form bound to the POST data
		if 類型表格.is_valid():
			類型 = 類型表格.save()
			return redirect('加類型表表格')
	else:
		類型表格 = 顯示類型表表格()

	揣著類型 = 類型表.objects.all()
	return render(request, '海外頁面/新語言.html', {
		'語言': 類型表格,
		'揣著語言':揣著類型,
		'介面名': '加類型表表格'
	})

def 類型表全部json(request):
	全部類型=[]
	for 揣著類型 in 類型表.objects.all():
		全部類型.append(揣著類型.類型)
	return HttpResponse(json.dumps(全部類型), content_type="application/json")


def 加原始語料表表格(request):
	if request.method == 'POST':  # If the form has been submitted...
		原始語料表格 = 顯示原始語料表表格(request.POST)  # A form bound to the POST data
		if 原始語料表格.is_valid():
			原始語料 = 原始語料表格.save()
			return redirect('加原始語料表表格')
	else:
		原始語料表格 = 顯示原始語料表表格()

	揣著原始語料 = 原始語料表.objects.all()
	return render(request, '海外頁面/新語料.html', {
		'語料': 原始語料表格,
		'揣著語料':揣著原始語料,
	})

def 顯示全部語料(request, 想看的語言, 想看的類型='單詞'):
	全部原始語料=原始語料表.objects.filter(語言表__語言=想看的語言, 類型表__類型=想看的類型)
	return render(request, '海外頁面/顯示全部語料.html', {
		'揣著語料':全部原始語料,
	})

def index初始顯示語言(request, 想看的語言=None):
	if 想看的語言 == None:
		想看的語言 = 語言表.objects.order_by('pk').first().語言
	print(想看的語言)			
	return render(request, '海外頁面/index.html', {
		'初始顯示語言':想看的語言,
	})		

# def 上傳檔案(request):
# 	if request.method == 'POST':
# 		form = 上傳檔案表格(request.POST, request.FILES)
# 		if form.is_valid():
# 			# 	存了輸入表格的資料後，回傳一筆資料的索引，可以修改它再回存
# 			原始檔案 = form.save()
# 			原始檔案.原始檔名 = request.FILES['原始檔'].name
# 			原始檔案.save()
# 			return redirect('上傳檔案')
# 	else:
# 		form = 上傳檔案表格(initial = {"原始檔名": "blahblah"})
# 		return render(request, '海外頁面/上傳檔案.html', {'form':form})

def 顯示原始語料表(request):
	揣著語料 = 原始語料表.objects.all()
	print(揣著語料)
	return render(request, '海外頁面/顯示原始語料表.html', {
		'揣著語料':揣著語料,
	})

	
def 揣著語料的全部檔案(request, 語料編號):
	a = 原始語料表.objects.filter(pk=語料編號).first()
	if request.method == 'POST':
		上傳表格 = 上傳檔案表格(request.POST, request.FILES)
		if 上傳表格.is_valid():
			# 	存了輸入表格的資料後，回傳一筆資料的索引，可以修改它再回存
			原始檔案 = 上傳表格.save()
			原始檔案.原始檔名 = request.FILES['原始檔'].name
			原始檔案.save()
	else:
		上傳表格 = 上傳檔案表格(initial = {"語料表":a })
		# fail:	上傳表格.fields['語料表'].widget.attrs['disabled'] = True
		
	# 	檢查EXCEL的數量，格式
	excel檔名陣列 = a.揣出excel檔()
	xlsx檔名 = None
	內容json = None
	字數 = a.類型表.揣字數()
	if len(excel檔名陣列) == 0:
		excel錯誤資訊 = '此語料無excel檔，請補上傳'
	elif len(excel檔名陣列) > 1:
		excel錯誤資訊 = '此語料excel檔有{0}個，請刪掉多餘的'.format(len(excel檔名陣列))
	else:	
		xlsx檔名 = excel檔名陣列[0]
		xlsx完整路徑檔名 = os.path.join(MEDIA_ROOT, xlsx檔名)
		xlsx內容陣列 = 把EXCEL讀進來(xlsx完整路徑檔名)
		內容json = xlsx陣列轉json(xlsx內容陣列, int(字數))
		if isinstance(xlsx內容陣列, str):
			excel錯誤資訊 = xlsx內容陣列
		elif isinstance(內容json, str):
			excel錯誤資訊 = 內容json
		else:
			excel錯誤資訊 = None
	
	wav和textgrid = a.揣出wav和textgrid檔()
	比對錯誤的表 = None
	比對錯誤的字格 = None
	串聯音標json = None
	try:
		# 	檢查是否有一組音檔與文字檔
		# 比對textgrid的音標和excel的IPA是否相符
		wav和textgrid錯誤資訊 = a.是否一組wav和textgrid()
		textgrid檔名陣列 = a.揣出textgrid檔()
		串聯音標json = 串聯多個文字檔的音標(textgrid檔名陣列)
		try:
			textgrid比對EXCEL(xlsx完整路徑檔名, 串聯音標json)
		except Exception as 錯誤:
			print('lalalala{0}'.format(錯誤.args))
			比對錯誤的表, 比對錯誤的字格 = 錯誤.args
	except Exception as 錯誤:
		wav和textgrid錯誤資訊 = 錯誤 
		
	return render(request, '海外頁面/顯示全部檔案.html', {
		'揣著語料': a.揣出語料的所有檔案(),
		'xlsx檔名': xlsx檔名,
 		'字數': 字數,
 		'內容json': 內容json,
 		'excel錯誤資訊': excel錯誤資訊,
 		'上傳表格': 上傳表格,
 		'語料編號': 語料編號, 
 		'wav和textgrid': wav和textgrid,
 		'wav和textgrid錯誤資訊': wav和textgrid錯誤資訊,
 		'串聯音標json':串聯音標json,
		'比對錯誤的表':比對錯誤的表,
		'比對錯誤的字格':比對錯誤的字格
	})

def 顯示xlsx的音(request,  xlsx檔名, 字數):
	全部的音 = []
	xlsx完整路徑檔名 = os.path.join(MEDIA_ROOT, xlsx檔名)
	#目前先預設單詞=1, 事後再補模型
	xlsx陣列 = 把EXCEL讀進來(xlsx完整路徑檔名)
	音json = xlsx陣列轉json(xlsx陣列, int(字數))
	return HttpResponse(json.dumps(音json), content_type="application/json")

# 因為可能有很多個wav和textgrid組，它們加起來才是EXCEL全部的IPA
def 串聯多個文字檔的音標(textgrid檔名陣列):
	串聯音標json = []
	for 文字檔 in  textgrid檔名陣列:
		路徑 = os.path.join(MEDIA_ROOT, 文字檔)
		串聯音標json +=流程(os.path.join(路徑))
	return 串聯音標json 

def 流程(文字檔路徑):
	資料 = 取出聲音位置(文字檔路徑)
# 	檢查輸入字串 = 檢查輸入(聲音檔路徑, 文字檔路徑, 資料[-1][-1])
# 	if(檢查輸入字串 != 'OK'):
# 		raise RuntimeError(檢查輸入字串)
	合併位置的資料 = 合併位置(資料)
	檢查大小字串 = 檢查位置大小(合併位置的資料)
	if(檢查大小字串 != 'OK'):
		raise RuntimeError(檢查大小字串)
	純音標與時區 = 合併音標(合併位置的資料)
	return 純音標與時區

def textgrid比對EXCEL(xlsx完整路徑檔名, 串聯音標json):
	結果, 資訊 = 音標比對excel(xlsx完整路徑檔名, 串聯音標json)
	return 結果, 資訊 

def 刪除一個檔案(request, 檔案編號):
	錯誤 = ''
	if request.method == 'GET':
		檔案列 = 原始檔案表.objects.filter(pk=檔案編號).first()
		if 檔案列 == None:
			錯誤 = '此檔不存在'
		else:
			try:
				os.remove(os.path.join(MEDIA_ROOT, 檔案列.原始檔.name))
				檔案列.delete()
			except:
				錯誤 = '無法刪除此檔'
				raise RuntimeError(錯誤)
	return HttpResponse(錯誤, content_type="text/plain; charset=UTF-8")