import unittest
import os
from NativeDB_py.檢查輸入的檔案 import 檢查輸入
from NativeDB_py.取出聲音位置 import 取出聲音位置


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'..','NativeDB_py')
	def tearDown(self):
		pass
	
	def test_單音(self):
		試驗音檔路徑 =os.path.join(self.檔案所在,'Penang_Y_M01_01.wav')
		試驗文字檔路徑  = os.path.join(self.檔案所在 ,'textgrid','Penang_Y_M01_01.TextGrid')
		寫出結果 = 取出聲音位置(試驗文字檔路徑)
		文字檔秒數 = 寫出結果[-1][-1] 
		答案 = 'OK'
		結果 = 檢查輸入(試驗音檔路徑, 試驗文字檔路徑, 文字檔秒數)
		self.assertEqual(結果, 答案)
		
if __name__=='__main__':
	unittest.main()