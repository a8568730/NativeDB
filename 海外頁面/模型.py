from django.db import models

# 華語 閩南 客話
class 語言表(models.Model):
	語言 = models.CharField(max_length=100)
	def __str__(self):
		return self.語言

# 單詞, 雙詞, 故事
class 類型表(models.Model):
	類型 = models.CharField(max_length=100)
	def __str__(self):
		return self.類型

class 原始語料表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語言表 = models.ForeignKey('語言表', related_name='原始語料表')
	類型表 = models.ForeignKey('類型表', related_name='原始語料表')
	所在 = models.CharField(max_length=300)
	年歲 = models.CharField(max_length=255)
	性別 = models.CharField(max_length=10, choices=[('查埔', '先生'), ('查某', '細妹')])
	def __str__(self):
		return self.語言表.語言 + ' ' + self.類型表.類型

class 原始檔案表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語料表 = models.ForeignKey('原始語料表', related_name='原始檔案表')
	原始檔名 = models.CharField(max_length=255)
	def __str__(self):
		return self.語料表 + ' ' + self.原始檔名

class 轉好的表(models.Model):
	頭一擺翻譯時間 = models.DateField(auto_now_add=True)
	上尾修改時間 = models.DateField(auto_now=True)
	語料表 = models.ForeignKey('原始語料表', related_name='轉好的表')
	漢字 = models.CharField(max_length=20000)
	IPA = models.CharField(max_length=20000)
	音檔 = models.CharField(max_length=100)
	def __str__(self):
		return self.漢字 + ' ' + self.IPA + ' ' + self.音檔
