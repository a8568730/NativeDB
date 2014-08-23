
import unittest
from NativeDB_py.合併音節的位置 import 合併位置

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	def test_合併(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'], '1.7946093688657765','2.02')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
		
	def test_合併xxx(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("XXX", '1.7946093688657765', '1.8053691896633992'),
		("XXX", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		答案 = [(['C1-(to)ʔ(8)-1'], '1.9583977521184779','2.02')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
	
	def test_合併多(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '4.38'),
		("C1-t(oʔ8)-1", '4.38', '5'),
		("V1-(t)o(ʔ8)-1", '5', '6.6'),
		("C1-(to)ʔ(8)-1", '6.6', '7.7'),
		("XXX", '7.7', '18.38'),
		("C1-t(oʔ8)-1", '18.38', '19.053691896633992'),
		("V1-(t)o(ʔ8)-1", '19.053691896633992', '20'),
		("C1-(to)ʔ(8)-1", '20', '20.2'),
		("XXX", '20.2', '33.8')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'], '1.7946093688657765','2.02'),
				(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'], '4.38','7.7'),
				(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'], '18.38','20.2')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
	
	def test_合併_中間有xxx(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '2.38'),
		("C1-t(oʔ8)-1", '2.38', '5'),
		("V1-(t)o(ʔ8)-1", '5', '6.6'),
		("C1-(to)ʔ(8)-1", '6.6', '7.7'),
		("XXX", '7.7', '18.38')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1','C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'],
				'1.7946093688657765','7.7')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
	
	
	def test_合併2_中間有兩xxx(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '2.18'),
		("XXX", '2.18', '2.38'),
		("C1-t(oʔ8)-1", '2.38', '5'),
		("V1-(t)o(ʔ8)-1", '5', '6.6'),
		("C1-(to)ʔ(8)-1", '6.6', '7.7'),
		("XXX", '7.7', '18.38')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1','C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'],
				'1.7946093688657765','7.7')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
		
	
	def test_合併_中間有四xxx(self):
		問題 = [("XXX" ,'0', '1.7946093688657765'),
		("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '2.38'),
		("XXX", '2.38', '2.68'),
		("XXX", '2.68', '2.98'),
		("XXX", '2.98', '4.38'),
		("C1-t(oʔ8)-1", '4.38', '5'),
		("V1-(t)o(ʔ8)-1", '5', '6.6'),
		("C1-(to)ʔ(8)-1", '6.6', '7.7'),
		("XXX", '7.7', '18.38')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'],'1.7946093688657765','2.02'),
			(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'],'4.38','7.7')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
		
	def test_合併開頭沒有XXX(self):
		問題 = [("C1-t(oʔ8)-1", '1.7946093688657765', '1.8053691896633992'),
		("V1-(t)o(ʔ8)-1", '1.8053691896633992', '1.9583977521184779'),
		("C1-(to)ʔ(8)-1", '1.9583977521184779', '2.02'),
		("XXX", '2.02', '3.38')
		]
		答案 = [(['C1-t(oʔ8)-1','V1-(t)o(ʔ8)-1','C1-(to)ʔ(8)-1'], '1.7946093688657765','2.02')]
		結果 = 合併位置(問題)
		self.assertEqual(結果, 答案)
	
		
if __name__=='__main__':
	unittest.main()