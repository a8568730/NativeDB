import unittest
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json 

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
# 	'你試驗足完整！！！'
# 	單詞
	def test_單詞(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
			]
		答案 =  [{"Num":"Zhang_VT_001",
				"Word":"(乖)巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"}]
# 		答案 = 'OK'
		結果 = xlsx陣列轉json(問題, 1)
		self.assertEqual(答案, 結果)
		
	def test_欄位不到四個(self):
		問題 = [
				['Num','Word'],
				['Zhang_VT_001','(乖)巧']
			]
		答案 =  'xlsx檔要四個欄位: Num, Word, IPA, Note'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)

	def test_欄位打錯字(self):
		問題 = [
				['Num','Word','xxx','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
			]
		答案 =  '第1列第3個欄位應為IPA'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)	
		
# 	Num欄位
	def test_單詞編號不一致(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
				['_VT_002','(乖)','kʰa3','kʰa3']
			]
		答案 =  'row(3)的Num欄位有誤'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
			
	def test_單詞編號內含數字(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang2_VT_001','(乖)巧','kʰa3','kʰa3'],
				['Zhang2_VT_002','(乖)巧','kʰa3','kʰa3']
			]
# 		答案 =  'OK'
		答案 =  [{"Num":"Zhang2_VT_001",
				"Word":"(乖)巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
				{"Num":"Zhang2_VT_002",
				"Word":"(乖)巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
			]
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
		
# 	Word欄位			
	def test_單詞字數不符(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','(乖)','kʰa3','kʰa3']
 			]
		答案 =  'row(3)的Word欄位格式不符'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)

	def test_單詞空字串(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','','kʰa3','kʰa3']
 			]
		答案 =  'row(3)的Word欄位空白'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)

	def test_單詞字有特殊符號(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang2_VT_001','(乖)巧$','kʰa3','kʰa3'],
				['Zhang2_VT_002','(乖)巧','kʰa3','kʰa3']
			]
		答案 =  'row(2)的Word欄位含特殊符號'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
		
	def test_單詞少一個括號(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','(乖巧','kʰa3','kʰa3']
 			]
		答案 =  'row(3)的Word欄位格式不符'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)			
	
	def test_單詞只有括號內有字(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
				['Zhang_VT_002','(乖)','kʰa3','kʰa3']
			]
		答案 =  'row(3)的Word欄位格式不符'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)	
		
	
# 	def test_單詞格式右(self):
# 		問題 = [
# 				['Num','Word','IPA','Note'],
# 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
# 			]
# 		答案 =  'OK'
# 		結果 = xlsx陣列轉json(問題, 1)
# 		self.assertEqual(答案, 結果)
# 	
	def test_單詞格式左(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','巧(乖)','kʰa3','kʰa3']
			]
# 		答案 =  'OK'
		答案 = [{"Num":"Zhang_VT_001",
				"Word":"巧(乖)",	
				"IPA":"kʰa3",
				"Note":"kʰa3"}]
		結果 = xlsx陣列轉json(問題, 1)
		self.assertEqual(答案, 結果)
	
	def test_單詞格式純(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','巧','kʰa3','kʰa3']
			]
		答案 = [{"Num":"Zhang_VT_001",
				"Word":"巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"}]
		結果 = xlsx陣列轉json(問題, 1)
		self.assertEqual(答案, 結果)
	
	def test_單詞格式X(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(巧)','kʰa3','kʰa3']
			]
		答案 =  'row(2)的Word欄位格式不符'
		結果 = xlsx陣列轉json(問題, 1)
		self.assertEqual(答案, 結果)
	
	def test_單詞格式兩邊(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(喔)巧(乖)','kʰa3','kʰa3']
			]
		答案 = [{"Num":"Zhang_VT_001",
				"Word":"(喔)巧(乖)",	
				"IPA":"kʰa3",
				"Note":"kʰa3"}]
		結果 = xlsx陣列轉json(問題, 1)
		self.assertEqual(答案, 結果)
# 		
	def test_雙詞格式純(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','乖巧','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔','kʰa3','kʰa3']
			]
# 		答案 =  'OK'
		答案 =  [{"Num":"Zhang_VT_001",
				"Word":"乖巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
				{"Num":"Zhang_VT_002",
				"Word":"喔喔",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
			]
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
		
	def test_雙詞格式左和右(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(喔)乖巧','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔()','kʰa3','kʰa3']
			]
# 		答案 =  'OK'
		答案 =  [{"Num":"Zhang_VT_001",
				"Word":"(喔)乖巧",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
				{"Num":"Zhang_VT_002",
				"Word":"喔喔()",	
				"IPA":"kʰa3",
				"Note":"kʰa3"},
			]
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
	
	def test_雙詞格式X(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','喔(乖)巧','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔(乖)','kʰa3','kʰa3']
			]
		答案 =  'row(2)的Word欄位格式不符'
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
		
	def test_雙詞格式X2(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(喔)乖(巧)','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔(乖)','kʰa3','kʰa3']
			]
		答案 =  'row(2)的Word欄位格式不符'
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)	
# 	只有一個字
# IPA只有一個音
# IPA格式有誤 (這能檢查嗎?)
# 如果以後有三個音、四個音....??

if __name__=='__main__':
	unittest.main()