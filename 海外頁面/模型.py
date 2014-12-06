from django.db import models
import os
from hai2gua7.settings import MEDIA_ROOT
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json
from itertools import chain

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
		#	找法1. 
		揣著全部檔案 = self.揣出語料的所有檔案()
		excel檔名陣列 = []
		for 檔案 in 揣著全部檔案: 
			if(檔案.副檔名() == 'xlsx' or 檔案.副檔名() == 'xls'):
				excel檔名陣列.append(檔案.原始檔名)
		return excel檔名陣列
	def 揣出wav檔(self):
		#	找法2. 	直接看全~~部檔案的表(來源可能是各種語料)
		揣著全部檔案 = 原始檔案表.objects.filter(語料表__pk=self.pk, 原始檔名__iendswith='wav')	
		wav檔名陣列 = []
		for 檔案 in 揣著全部檔案: 
			wav檔名陣列.append(檔案.原始檔名)
		return wav檔名陣列
	def 揣出textgrid檔(self):
		#	找法3. 此語料自己指回去的檔案們組成的檔案表
		揣著全部檔案 = self.原始檔案表.filter(原始檔名__iendswith='TextGrid')	
		textgrid檔名陣列 = []
		for 檔案 in 揣著全部檔案: 
			textgrid檔名陣列.append(檔案.原始檔名)
		return textgrid檔名陣列
	def 揣出wav和textgrid檔(self):
		wav = self.揣出wav檔()
		grid = self.揣出textgrid檔()
		wav和grid檔名陣列 = list(chain(wav, grid))
		return sorted(wav和grid檔名陣列)
	def 是否一組wav和textgrid(self):
		wav檔名陣列 = self.揣出wav檔()
		textgrid檔名陣列 = self.揣出textgrid檔()
		wav集合 = set(wav檔名陣列)
		textgrid集合 = set(textgrid檔名陣列)
		if len(wav集合) < len(wav檔名陣列):
			raise RuntimeError('wav有檔名重複')
		elif len(textgrid集合) < len(textgrid檔名陣列):
			raise RuntimeError('TextGrid有檔名重複')
		else:
			# 	只比對檔名，能被減掉的代表有一組wav和textgrid
			#  檔名不一致
			wav集合 = {w.replace('.wav', '') for w in wav集合}
			textgrid集合 = {w.replace('.TextGrid', '') for w in textgrid集合}
			有缺的wav集合 = {w + '.wav' for w in wav集合 - textgrid集合}
			有缺的texgrid集合 = {w + '.TextGrid' for w in textgrid集合 - wav集合}
			if len(有缺的wav集合) > 0 or len(有缺的texgrid集合) > 0:
				raise RuntimeError('缺wav檔的: {1}, \n缺TextGrid檔的: {0}'.format(','.join(有缺的wav集合), ','.join(有缺的texgrid集合)))
		return
	
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
	漢字 = models.CharField(max_length=20000) #從EXCEL
	IPA = models.CharField(max_length=20000) #從EXCEL
	音檔 = models.FileField() #從切割的音檔
	def __str__(self):
		return self.漢字 + ' ' + self.IPA + ' ' + self.音檔
