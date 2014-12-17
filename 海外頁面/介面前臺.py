from django.http import HttpResponse
from 海外頁面.模型 import 語言表
import json
from 海外頁面.模型 import 轉好的表

def 顯示語言漢字相同的音檔(request, 語言名稱):
	# 按照前台主頁的需要排序
	# 輸出格式 {	
	#		MoT: [ [{word:字, IPA:音標, wavs:[音檔, 音檔]}] , 音檔數量], 
	# 		DiT: [ [{word:字字, IPA:音標, wavs:[音檔]}, {word:字字, IPA:音標, wavs:[音檔, 音檔, 音檔]}] , 音檔數量]
	# 	}
	陣列 = 轉好的表.objects.filter(語料表__語言表__語言=語言名稱).order_by('語料表__類型表__類型', '漢字', 'IPA')
	輸出 =  {}
	前一類型 = ""
	前一漢字 = ""
	前一IPA = ""
	
	for 一轉好 in 陣列:
		目前漢字 = 一轉好.漢字 
		目前類型 = 一轉好.語料表.類型表.類型
		目前IPA = 一轉好.IPA
		
		if 目前類型 == 前一類型:
			if 目前漢字 == 前一漢字 and 目前IPA == 前一IPA:
				# 同一個字新增此音檔
				輸出[目前類型][0][-1]['wavs'].append(一轉好.音檔.url)
				輸出[目前類型][1] = 輸出[目前類型][1] + 1
				pass
			else:
				# 新增下一個字
				輸出[目前類型][0].append( {'HanJi': 目前漢字, 'IPA':目前IPA,  'wavs':[一轉好.音檔.url]} )
				輸出[目前類型][1] = 輸出[目前類型][1] + 1
		else:
			#初始輸出 {} -> { [ MoT: [{word:字, IPA:音標, 音檔:[音檔]}], 1] }
			輸出[目前類型] = []
			輸出[目前類型].append( [{'HanJi': 目前漢字, 'IPA':目前IPA,  'wavs':[一轉好.音檔.url]}] )
			輸出[目前類型].append(1)
			
		前一漢字 = 目前漢字
		前一類型 = 目前類型
		前一IPA = 目前IPA
		
	return HttpResponse(json.dumps(輸出, ensure_ascii=False), content_type='application/json; charset=utf-8')


def 顯示同語言一漢字的所有音檔(request, 語言名稱, 漢字):
	輸出 = []
	return HttpResponse(json.dumps(輸出, ensure_ascii=False), content_type='application/json; charset=utf-8')
