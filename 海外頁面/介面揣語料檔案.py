from django.http.response import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from 海外頁面.模型 import 原始語料表
from 海外頁面.表格 import 上傳檔案表格
from hai2gua7.settings import MEDIA_ROOT
from 海外頁面.模型 import 原始檔案表
from os.path import os
import json
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json
from NativeDB_py.取出聲音位置 import 取出聲音位置
from NativeDB_py.檢查輸入的檔案 import 檢查輸入
from NativeDB_py.合併音節的位置 import 合併位置
from NativeDB_py.檢查取出的位置大小 import 檢查位置大小
from NativeDB_py.合併的音標比對excel import 音標比對excel
from NativeDB_py.合併音標 import 合併音標
from NativeDB_py.合併音標比對excel結果 import 檢查不合格的表與字格
from NativeDB_py.合併音標比對excel結果 import 輸出合格的表
import itertools
from 海外頁面.模型 import 轉好的表
from NativeDB_py.照位置切割音檔 import 切割音檔
from django.core.files.base import File, ContentFile
import wave
import io


def 揣著語料的全部檔案(request, 語料編號):
	此語料 = 原始語料表.objects.filter(pk=語料編號).first()
	if request.method == 'POST':
		上傳表格 = 上傳檔案表格(request.POST, request.FILES)
		if 上傳表格.is_valid():
			# 	存了輸入表格的資料後，回傳一筆資料的索引，可以修改它再回存
			原始檔案 = 上傳表格.save()
			原始檔案.原始檔名 = request.FILES['原始檔'].name
			原始檔案.save()
	else:
		上傳表格 = 上傳檔案表格(initial={"語料表":此語料 })
		# fail:	上傳表格.fields['語料表'].widget.attrs['disabled'] = True
		
	# 	檢查EXCEL的數量，格式
	xlsx錯誤資訊, xlsx檔名, xlsx完整路徑檔名, 內容json = 檢查EXCEL的內頁數與格式(此語料)
	字數 = 此語料.類型表.揣字數()
	# 	檢查是否有一組音檔與文字檔
	wav和textgrid錯誤資訊, wav和textgrid, 串聯音標json = 檢查音檔與字格(此語料)
	#  檢查textgrid的音標和excel的IPA是否相符
	if 串聯音標json != None:
		比對錯誤的表, 比對錯誤的字格 = 檢查EXCEL與字格(xlsx完整路徑檔名, 串聯音標json)
	else:
		比對錯誤的表, 比對錯誤的字格 = None, None
				
	return render(request, '海外頁面/顯示全部檔案.html', {
		'揣著語料': 此語料.揣出語料的所有檔案(),
		'語料編號': 語料編號,
 		'類型': 此語料.類型表.類型,
 		'上傳表格': 上傳表格,
 		'xlsx檔名': xlsx檔名,
		'字數': 字數,
 		'xlsx錯誤資訊': xlsx錯誤資訊,
 		'內容json': 內容json,
 		'wav和textgrid錯誤資訊': wav和textgrid錯誤資訊,
 		'wav和textgrid': wav和textgrid,
 		'串聯音標json':串聯音標json,
		'比對錯誤的表':比對錯誤的表,
		'比對錯誤的字格':比對錯誤的字格
	})

def 刪除一個檔案(request, 檔案編號):
	# 刪單一檔功能
	錯誤 = ''
	if request.method == 'GET':
		檔案列 = 原始檔案表.objects.filter(pk=檔案編號).first()
		if 檔案列 == None:
			錯誤 = '此檔不存在'
		else:
			try:
				# 	刪除資料本體和資料庫的一筆檔案資料
				os.remove(os.path.join(MEDIA_ROOT, 檔案列.原始檔.name))
				檔案列.delete()
			except:
				錯誤 = '無法刪除此檔'
				raise RuntimeError(錯誤)
	return HttpResponse(錯誤, content_type="text/plain; charset=UTF-8")

def 測試抓網址(request, 語料編號):
	# 測試angularjs可以抓到網址參數
	template = loader.get_template('海外頁面/測試抓網址.html')
	context = RequestContext(request, {'語料編號':語料編號})
	return HttpResponse(template.render(context))

def 測試批次刪除(request, 語料編號):
	# 測試刪除檔案時網頁會直接跟著刪去一筆資料
	template = loader.get_template('海外頁面/測試批次刪除.html')
	context = RequestContext(request, {'語料編號':語料編號})
	return HttpResponse(template.render(context))	

def 顯示xlsx的音(request, xlsx檔名, 字數):
	全部的音 = []
	xlsx完整路徑檔名 = os.path.join(MEDIA_ROOT, xlsx檔名)
	# 目前先預設單詞=1, 事後再補模型
	xlsx陣列 = 把EXCEL讀進來(xlsx完整路徑檔名)
	音json = xlsx陣列轉json(xlsx陣列, int(字數))
	return HttpResponse(json.dumps(音json), content_type="application/json")

def 串聯多個文字檔的音標(textgrid檔名陣列):
	# 可能有很多個wav和textgrid組，它們加起來才是EXCEL全部的IPA
	串聯音標json = []
	for 文字檔 in  textgrid檔名陣列:
		路徑 = os.path.join(MEDIA_ROOT, 文字檔)
		串聯音標json.append(流程(os.path.join(路徑)))
	return 串聯音標json 

def 流程(文字檔路徑):
	# 找出一個Textgrid的IPA
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

def 語料的全部檔案json(request):
	語料編號 = request.GET['pk']
	語料列 = 原始語料表.objects.filter(pk=語料編號).first()
	檔案陣列 = []
	for 檔案列 in 語料列.揣出語料的所有檔案():
		檔案陣列.append([檔案列.pk, 檔案列.原始檔名])
	return HttpResponse(json.dumps(檔案陣列), content_type="application/json")
	
def 檢查EXCEL的內頁數與格式(此語料):
	xlsx檔名陣列 = 此語料.揣出excel檔()
	字數 = 此語料.類型表.揣字數()
	xlsx檔名 = None
	內容json = None
	xlsx完整路徑檔名 = ''
	if len(xlsx檔名陣列) == 0:
		xlsx錯誤資訊 = '此語料無excel檔，請補上傳'
	elif len(xlsx檔名陣列) > 1:
		xlsx錯誤資訊 = '此語料excel檔有{0}個，請刪掉多餘的'.format(len(xlsx檔名陣列))
	else:	
		xlsx檔名 = xlsx檔名陣列[0]
		xlsx完整路徑檔名 = os.path.join(MEDIA_ROOT, xlsx檔名)
		xlsx內容陣列 = 把EXCEL讀進來(xlsx完整路徑檔名)
		內容json = xlsx陣列轉json(xlsx內容陣列, int(字數))
		if isinstance(xlsx內容陣列, str):
			xlsx錯誤資訊 = xlsx內容陣列
		elif isinstance(內容json, str):
			xlsx錯誤資訊 = 內容json
		else:
			xlsx錯誤資訊 = None
	return 	xlsx錯誤資訊, xlsx檔名, xlsx完整路徑檔名, 內容json

def 檢查音檔與字格(此語料):
	# 	檢查是否有一組音檔與文字檔
	wav和textgrid = 此語料.揣出wav和textgrid檔()
	比對錯誤的表 = None
	比對錯誤的字格 = None
	串聯音標json = None
	try:
		wav和textgrid錯誤資訊 = 此語料.是否一組wav和textgrid()
		textgrid檔名陣列 = 此語料.揣出textgrid檔()
		串聯音標json = 串聯多個文字檔的音標(textgrid檔名陣列)
	except Exception as 錯誤:
		wav和textgrid錯誤資訊 = 錯誤 
		# raise #debug用的
	return wav和textgrid錯誤資訊, wav和textgrid, 串聯音標json

def 檢查EXCEL與字格(xlsx完整路徑檔名, 串聯音標json):
	# 比對textgrid的音標和excel的IPA是否相符
	啾啾砲 = list(itertools.chain.from_iterable(串聯音標json))
	try:
		檢查不合格的表與字格(xlsx完整路徑檔名, 啾啾砲)
	except Exception as 錯誤:
		# 錯誤一. 缺檔案
		# 錯誤二. 比對
		print(錯誤.args)
		比對錯誤的表, 比對錯誤的字格 = 錯誤.args
		# raise #debug用的
	return 比對錯誤的表, 比對錯誤的字格


def 顯示合格的EXCEL與字格(request, 語料編號):
	# 顯示出textgrid的音標和excel比對成功的漢字與拼音
	此語料 = 原始語料表.objects.filter(pk=語料編號).first()
	# 	檢查EXCEL的數量，格式
	xlsx錯誤資訊, xlsx檔名, xlsx完整路徑檔名, 內容json = 檢查EXCEL的內頁數與格式(此語料)
	字數 = 此語料.類型表.揣字數()
	# 	檢查是否有一組音檔與文字檔
	wav和textgrid錯誤資訊, wav和textgrid, 串聯音標json = 檢查音檔與字格(此語料)
	#  檢查textgrid的音標和excel的IPA是否相符
	啾啾砲 = list(itertools.chain.from_iterable(串聯音標json))
	合格的漢字與拼音 = 輸出合格的表(xlsx完整路徑檔名, 啾啾砲)
	
	# 找出全部對應的字格檔名與時間
	合格的綜合陣列 = []
	for 一個檔名, 一個檔的音標json in zip(此語料.揣出textgrid檔(), 串聯音標json):
		# 		print('a={0}, b={1}'.format(a,b))
		# 利用拼音，將檔名與時間，漢字合成一列
		for 音標json in 一個檔的音標json: 
			音標 = ''.join(音標json[0])
			開頭時間 = 音標json[1]
			結尾時間 = 音標json[2]
			for 一個合格 in 合格的漢字與拼音:
				if 音標 == 一個合格[1]:
					合格的綜合陣列.append([一個合格, 一個檔名, 開頭時間, 結尾時間])
					切割音檔並建表(語料編號, 一個合格[0], 一個合格[1], 一個檔名, 開頭時間, 結尾時間)
	
	return render(request, '海外頁面/顯示全部語料.html', {
			'揣著語料':合格的綜合陣列
	})
	
def 切割音檔並建表(語料編號, 漢字, 拼音, 字格檔名, 開頭時間, 結尾時間):
	# 0. 判斷是否已切過
	一個轉好表 = 轉好的表.objects.filter(語料表__pk=語料編號).filter(IPA=拼音).first()
	# 1. 若無，切割
	if 一個轉好表 == None or True: 
		try: 
			被切割音檔名 = os.path.splitext(字格檔名)[0] + '.wav'
			被切割音檔路徑 = os.path.join(MEDIA_ROOT, 被切割音檔名)
			完成音檔名 = 漢字 + '_' + 被切割音檔名
			完成音檔完整路徑 = os.path.join(MEDIA_ROOT, 完成音檔名)  
			
			完成檔指標 = io.BytesIO()
			切割音檔(被切割音檔路徑, 完成檔指標, 開頭時間, 結尾時間)
			# 2. 加入資料庫
			此語料表 = 原始語料表.objects.get(pk=語料編號)
# 			完成音檔 = wave.open(完成音檔完整路徑)
			欲存的表 = 轉好的表(語料表=此語料表, 漢字=漢字, IPA=拼音)
# 			if 欲存的表.is_valid():
			欲存的表.音檔.save(完成音檔名, File(完成檔指標), save=True)
# 			print(type(欲存的表.音檔))
# 			print(欲存的表.音檔.url)
# 			print(欲存的表.音檔.delete())
# 			欲存的表.音檔.save(完成音檔名,  ContentFile("esta sentencia está en español"))
# 			欲存的表.save()
			完成檔指標.close()
# 			完成音檔.close()
		except Exception as 錯誤:
			raise
