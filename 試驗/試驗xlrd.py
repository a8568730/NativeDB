import unittest
import os
from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'試驗資料')
	def tearDown(self):
		pass
	def test_基本short(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'numberbook2.xlsx')
		答案 = [
					['Num','Word','IPA','Note'],
					['Zhang_VT_001','(乖)巧'	, 'kʰa3','kʰa3']
				]
		結果 = 把EXCEL讀進來(試驗檔名)
		self.assertEqual(答案, 結果)
	
	def test_基本long(self):
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
		結果 = 把EXCEL讀進來(試驗檔名)
		self.assertEqual(答案, 結果)
		
if __name__=='__main__':
	unittest.main()