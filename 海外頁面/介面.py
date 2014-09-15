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
	return render(request, '海外頁面/新語言.html', {
		'語言': 原始語料表格,
		'揣著語言':揣著原始語料,
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

def 上傳檔案(request):
	if request.method == 'POST':
		form = 上傳檔案表格(request.POST, request.FILES)
		if form.is_valid():
#			 處理上傳後的檔案(request.FILES['file'])
#			 return HttpResponseRedirect('/success/url/')
			原始檔案 = form.save()
			return redirect('上傳檔案')
	else:
		form = 上傳檔案表格()
			
# 	args = {}
# 	args['form'] = form		
	return render(request, '海外頁面/上傳檔案.html', {'form':form})

# def 處理上傳後的檔案(f):
#	 with open('some/file/name.txt', 'wb+') as destination:
#		 for chunk in f.chunks():
#			 destination.write(chunk)