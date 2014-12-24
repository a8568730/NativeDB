import unittest
import os
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'..','NativeDB_py')
	def tearDown(self):
		pass
	
	def test_單音(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook2.xlsx')
		答案 = [
					['Num','Word','IPA','Note'],
					['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
		]
		結果 = 把EXCEL讀進來(試驗檔名)
		self.assertEqual(結果, 答案)
	
	def test_textgrid(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'Penang_M_M01_correct.xlsx')
		答案 = '警告：excel檔的sheet超過一頁，請重新上傳'
		結果 = 把EXCEL讀進來(試驗檔名)
		self.assertEqual(結果, 答案)

	def test_單音Note應為8沒有小數點(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook5.xlsx')
		答案 = [
					['Num','Word','IPA','Note'],
					['Rd067','鸡婆','kue1po2','8'],
					['Rd068','鸡公','kue1kan1','8.2']
		]
		結果 = 把EXCEL讀進來(試驗檔名)
		self.assertEqual(結果, 答案)
			
if __name__=='__main__':
	unittest.main()