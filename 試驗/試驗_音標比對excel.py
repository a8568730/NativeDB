import unittest
from NativeDB_py.合併的音標比對excel import 音標比對excel


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	def test_比對_桌1(self):
		檔案 = '../NativeDB_py/numberbook1.xlsx'
		問題 = [(['toʔ8'], '1.7946093688657765', '2.02')]
		答案 = True
		結果 = 音標比對excel(檔案, 問題)
		self.assertEqual(答案, 結果)
		
	def test_比對_記者交保(self):
		檔案 = '../NativeDB_py/numberbook3.xlsx'
		問題 = [(['ki5','tsia3'], '1.7946093688657765', '2.02'), (['kau1', 'po3'], '4.38', '7.7')]
		答案 = True
		結果 = 音標比對excel(檔案, 問題)
		self.assertEqual(答案, 結果)
	
	def test_比對_雞婆(self):
		檔案 = '../NativeDB_py/numberbook4.xlsx'
		問題 = [(['ke1','po2'], '1.7946093688657765', '7.7')]
		答案 = False
		結果 = 音標比對excel(檔案, 問題)
		self.assertEqual(答案, 結果)
		
if __name__ == '__main__':
	unittest.main()
