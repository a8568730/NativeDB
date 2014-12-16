from django.http import HttpResponse
from 海外頁面.模型 import 語言表
import json
from 海外頁面.模型 import 轉好的表

def 顯示語言漢字相同的音檔(request, 語言名稱):
	陣列 = 轉好的表.objects.filter(語料表__語言表__語言=語言名稱).order_by('漢字', 'IPA')
	輸出 = []
	for 一轉好 in 陣列:
		輸出.append([一轉好.漢字, 一轉好.IPA, 一轉好.音檔.url])
	return HttpResponse(json.dumps(輸出, ensure_ascii=False), content_type='application/json; charset=utf-8')