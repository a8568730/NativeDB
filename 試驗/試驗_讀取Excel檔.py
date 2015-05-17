import unittest
import os
from NativeDB_py.讀取Excel檔 import 讀取Excel檔

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'試驗資料')
	def tearDown(self):
		pass
	
	def test_單音(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook2.xlsx')
		答案 = [
					['Num','Word','IPA','Note'],
					['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
		]
		結果 = 讀取Excel檔(試驗檔名)
		self.assertEqual(結果, 答案)
	
	def test_多個單音(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook.xlsx')
		答案 = [		
					['Num', 'Word', 'IPA', 'Note'],
					['Zhang_VT_001', '(乖)巧', 'kʰa3', 'kʰa3'],
					['Zhang_VT_002', '(肉)羹', 'kĩ1', 'kĩ1'],
					['Zhang_VT_003', '富(人)', 'pu5', 'x'],
					['Zhang_VT_004', '(醫)治', 'ti6', 'x'],
					['Zhang_VT_005', '(乖)巧', 'kʰa3', 'kʰa3'],
					['Zhang_VT_006', '(紅)茶', 'te2', 'te2'],
					['Zhang_VT_007', '(土)地', 'te6', 'te6'],
					['Zhang_VT_008', '(臭)殕(發霉)', 'pʰu3', 'pʰu3'],
					['Zhang_VT_009', '(監)督', 'tok7', 'tok7']
				]
		結果 = 讀取Excel檔(試驗檔名)
		self.assertEqual(答案, 結果)
		
	def test_工作表不可以超過一頁(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'Penang_M_M01_correct.xlsx')
		答案 = '警告：excel檔的sheet超過一頁，請重新上傳'
		結果 = 讀取Excel檔(試驗檔名)
		self.assertEqual(結果, 答案)

	def test_單音Note應為8沒有小數點(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook5.xlsx')
		答案 = [
					['Num','Word','IPA','Note'],
					['Rd067','鸡婆','kue1po2','8'],
					['Rd068','鸡公','kue1kan1','8.2']
		]
		結果 = 讀取Excel檔(試驗檔名)
		self.assertEqual(結果, 答案)
				
if __name__=='__main__':
	unittest.main()