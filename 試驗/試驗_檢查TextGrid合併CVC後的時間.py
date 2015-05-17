import unittest
from NativeDB_py.檢查TextGrid合併CVC後的時間 import 檢查TextGrid合併CVC後的時間


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_一般(self):
		問題 = [("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		答案 = 'OK'
		結果 = 檢查TextGrid合併CVC後的時間(問題)
		self.assertEqual(結果, 答案)
		
	def test_時間有誤(self):
		問題 = [("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.5053691896633992', '1.3583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		答案 = 'V1-(t)o(ʔ8)-1的開頭比前一結尾早'
		結果 = 檢查TextGrid合併CVC後的時間(問題)
		self.assertEqual(結果, 答案)

	
if __name__=='__main__':
	unittest.main()