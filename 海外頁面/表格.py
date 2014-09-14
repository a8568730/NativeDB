from django.forms import ModelForm
from django.forms import Textarea
from django.forms import Select
from 海外頁面.模型 import 語言表
from 海外頁面.模型 import 類型表
from 海外頁面.模型 import 原始語料表
from django import forms

# 決定HTML要顯示資料庫有的哪些資料

class 顯示語言表表格(ModelForm):
	class Meta:
		model = 語言表
		#	接著會根據模型.py，知道語言表有一個欄位：語言
		fields = '__all__'

class 顯示類型表表格(ModelForm):
	class Meta:
		model = 類型表
		fields = '__all__'

class 顯示原始語料表表格(ModelForm):
	class Meta:
		model = 原始語料表
		fields = '__all__'

class 上傳檔案表格(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
# class 加新文章表格(ModelForm):
# 	class Meta:
# 		model = 何澤政文章
# 		fields = ['分類', '原本標題', '原本內容', ]
# 		labels = {
# 			'分類':'分類',
#             '原本標題': '原始標題',
#             '原本內容': '原始內容',
#         }
# 		help_texts = {
#             '原本標題': '免斷詞',
#             '原本內容': '免斷詞',
#         }
# 		error_messages = {
#             '原本標題': {
#                 'max_length': ("This writer's name is too long."),
#             },
#         }
# 		widgets = {
# 			'分類': Select(choices=分類),
# 			'原本內容': Textarea(attrs={'class':'橫線','cols':'60'}),
# 		}
# 		
# class 改國語斷詞表格(ModelForm):
# 	class Meta:
# 		model = 何澤政文章
# 		fields = ['原本標題', '斷詞標題', '原本內容', '斷詞內容']
# 		widgets = {
# 			'原本內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 			'斷詞內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 		}
# 
# 
# class 改閩南語翻譯表格(ModelForm):
# 	class Meta:
# 		model = 何澤政文章
# 		fields = ['斷詞標題', '教羅標題', '斷詞內容', '教羅內容']
# 		widgets = {
# 			'斷詞內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 			'教羅內容': Textarea(attrs={'class':'文章 橫線','wrap': 'off'}),
# 		}
