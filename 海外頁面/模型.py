from django.db import models
import os
from hai2gua7.settings import MEDIA_ROOT
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json

# 決定資料庫有哪些表，各自有哪些欄位

# 華語 閩南 客話
class 語言表(models.Model):
	語言 = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.語言

# 單詞, 雙詞, 故事
class 類型表(models.Model):
	類型 = models.CharField(max_length=1000, unique=True)
# 	字數 = models.PositiveIntegerField(choices=[1,2,3,4,5,6,7,8,9,10,(10000,'故事')])
	def __str__(self):
		return str(self.pk) + self.類型
	def 揣字數(self):
		if(self.類型 == '單詞'):
			return 1
		elif(self.類型 == '雙詞'):
			return 2
		elif(self.類型 == '三字詞'):
			return 3
		elif(self.類型 == '故事'):
			return 10000
		return -1
	
class 原始語料表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語言表 = models.ForeignKey('語言表', related_name='原始語料表')
	類型表 = models.ForeignKey('類型表', related_name='原始語料表')
	所在 = models.CharField(max_length=300)
	年歲 = models.CharField(max_length=255, choices=[('青年','青年'), ('中年','中年'),('老年','老年')])
	性別 = models.CharField(max_length=10, choices=[('查埔', '先生'), ('查某', '細妹')])
	def __str__(self):
		return str(self.pk) + ' ' + self.語言表.語言 + '  ' + self.類型表.類型 + ' ' + self.所在 + ' ' + self.年歲 + ' ' + self.性別
	def 揣出語料的所有檔案(self):
		return 原始檔案表.objects.filter(語料表__pk=self.pk)
	def 揣出excel檔(self):
		揣著全部檔案 = self.揣出語料的所有檔案()
		excel檔名陣列 = []
		for 檔案 in 揣著全部檔案: 
			if(檔案.副檔名() == 'xlsx' or 檔案.副檔名() == 'xls'):
				excel檔名陣列.append(檔案.原始檔名)
		return excel檔名陣列
	
class 原始檔案表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語料表 = models.ForeignKey('原始語料表', related_name='原始檔案表')
	原始檔 = models.FileField()
	原始檔名 = models.CharField(max_length=255)
	def __str__(self):
		return str(self.pk) + ' ' + str(self.語料表) + ' ' + self.原始檔名
	def 副檔名(self):
		name, extension = os.path.splitext(self.原始檔.name)
		return extension[1:]
	
class 轉好的表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語料表 = models.ForeignKey('原始語料表', related_name='轉好的表')
	漢字 = models.CharField(max_length=20000)
	IPA = models.CharField(max_length=20000)
	音檔 = models.CharField(max_length=100)
	def __str__(self):
		return self.漢字 + ' ' + self.IPA + ' ' + self.音檔
