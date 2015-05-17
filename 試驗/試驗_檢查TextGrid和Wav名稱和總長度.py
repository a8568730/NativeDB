import unittest
import os
from NativeDB_py.讀取TextGrid檔 import 讀取TextGrid檔
from NativeDB_py.檢查TextGrid和Wav名稱和總長度 import 檢查TextGrid和Wav名稱和總長度 


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'試驗資料')
	def tearDown(self):
		pass
	
	def test_單音(self):
		試驗音檔路徑 =os.path.join(self.檔案所在,'Penang_Y_M01_01.wav')
		試驗文字檔路徑  = os.path.join(self.檔案所在 ,'textgrid','Penang_Y_M01_01.TextGrid')
		寫出結果 = 讀取TextGrid檔(試驗文字檔路徑)
		文字檔秒數 = 寫出結果[-1][-1] 
		答案 = 'OK'
		結果 = 檢查TextGrid和Wav名稱和總長度(試驗音檔路徑, 試驗文字檔路徑, 文字檔秒數)
		self.assertEqual(結果, 答案)
		
if __name__=='__main__':
	unittest.main()