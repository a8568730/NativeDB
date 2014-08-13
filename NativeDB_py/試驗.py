
import unittest
from NativeDB_py.取出聲音位置 import 取出聲音位置

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	def test_字(self):
		試驗檔名 ='Penang_Y_M01_01.TextGrid'
		答案 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		結果 = 取出聲音位置(試驗檔名)
		self.assertEqual(結果, 答案)

if __name__=='__main__':
	unittest.main()