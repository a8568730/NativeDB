
import unittest
from NativeDB_py.讀取TextGrid檔 import 讀取TextGrid檔
import os

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'試驗資料', 'textgrid')
	def tearDown(self):
		pass
	
	def test_單音(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'Penang_Y_M01_01.TextGrid')
		答案 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		結果 = 讀取TextGrid檔(試驗檔名)
		self.assertEqual(結果, 答案)
	
	def test_textgrid(self):
		試驗檔名  = os.path.join(self.檔案所在 ,'文字有空白.TextGrid')
		答案 = [("C2- ts(ioʔ8)-1" ,'1545.7859409529399', '1545.8649050790789'),
		("V2-( ts)io(ʔ8)-1", '1545.8649050790789', '1546.0228333313567'),
		("XXX", '1546.0228333313567', '1549.502375')
		]
		結果 = 讀取TextGrid檔(試驗檔名)
		self.assertEqual(結果, 答案)

if __name__=='__main__':
	unittest.main()