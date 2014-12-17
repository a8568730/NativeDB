from django.test import TestCase
from 海外頁面.模型 import 原始語料表
from 海外頁面.模型 import 轉好的表
from django.core.urlresolvers import reverse
# 
# class QuestionMethodTests(TestCase):
# 
#     def test_剛好一組wav和grid(self):
#         語料 = 原始語料表.objects.filter(pk=3).first()
#         問題 = 語料.
#         答案 = True 
#         self.assertEqual(問題, 答案)

# def 建立轉好的表(語料表, 漢字, IPA, 音檔名稱):
# 	return 轉好的表.objects.create(語料表=語料表, 漢字=漢字, IPA=IPA, 音檔=音檔名稱)
# 
# class QuestionMethodTests(TestCase):
# 	
# 	def test_顯示語言漢字相同的音檔(self):
# 		response = self.client.get(reverse('海外頁面:顯示語言漢字相同的音檔', kwargs={'語言名稱': '閩南語'}))
		