import unittest
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json 

class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
# 	單詞
# 	def test_單詞(self):
# 		問題 = [
# 				['Num','Word','IPA','Note'],
# 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',Word:'(乖)巧',	IPA:'kʰa3',Note:'kʰa3'}]"
# 		結果 = xlsx陣列轉json(問題, 1)
# 		self.assertEqual(答案, 結果)
		
	def test_單詞欄位不夠(self):
		問題 = [
				['Num','Word'],
				['Zhang_VT_001','(乖)巧']
			]
		答案 =  'xlsx檔要四個欄位: Num, Word, IPA, Note'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)

	def test_單詞欄位有誤(self):
		問題 = [
				['Num','Word','xxx','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
			]
		答案 =  'col(1,2)應為IPA'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)	
		
	def test_單詞編號不一致(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
				['_VT_002','(乖)','kʰa3','kʰa3']
			]
		答案 =  'col(2)的Num有誤'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
			
	def test_單詞編號內含數字(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang2_VT_001','(乖)巧','kʰa3','kʰa3'],
				['Zhang2_VT_002','(乖)巧','kʰa3','kʰa3']
			]
		答案 =  'OK'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
				
	def test_單詞字數不符(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','(乖)','kʰa3','kʰa3']
 			]
		答案 =  'col(2)的Word字數應為1'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)

	def test_單詞空字串(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','','kʰa3','kʰa3']
 			]
		答案 =  'col(2)沒有字'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
		
	def test_單詞括號有誤(self):
		問題 = [
 				['Num','Word','IPA','Note'],
 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
 				['Zhang_VT_002','(乖巧','kʰa3','kʰa3']
 			]
		答案 =  'col(2)的Word少了)'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)			
	
	def test_單詞字數有誤(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3'],
				['Zhang_VT_002','(乖)','kʰa3','kʰa3']
			]
		答案 =  'col(2)的Word字數應為1'
		詞數 = 1
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)	
		
	def test_雙詞字數正確2(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','(喔)乖巧','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔()','kʰa3','kʰa3']
			]
		答案 =  'OK'
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
	
	def test_雙詞字數錯誤(self):
		問題 = [
				['Num','Word','IPA','Note'],
				['Zhang_VT_001','喔(乖)巧','kʰa3','kʰa3'],
				['Zhang_VT_002','喔喔(乖)','kʰa3','kʰa3']
			]
		答案 =  'col(1)的Word字數應為2'
		詞數 = 2
		結果 = xlsx陣列轉json(問題, 詞數)
		self.assertEqual(答案, 結果)
	
				
# 	def test_單詞短(self):
# 		問題 = [
# 				['Num','Word','IPA','Note'],
# 				['Zhang_VT_001','(乖)巧','kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 	def test_單詞正常長(self):
# 		問題 = [		
# 				['Num', 'Word', 'IPA', 'Note'],
# 				['Zhang_VT_001', '(乖)巧', 'kʰa3', 'kʰa3'],
# 				['Zhang_VT_002', '(肉)羹', 'kĩ1', 'kĩ1'],
# 				['Zhang_VT_003', '富(人)', 'pu5', 'x'],
# 				['Zhang_VT_004', '(醫)治', 'ti6', 'x'],
# 				['Zhang_VT_005', '(乖)巧', 'kʰa3', 'kʰa3'],
# 			]
# 		答案 =  "[\
# 				{	Num:'Zhang_VT_001',\
# 					Word:'(乖)巧',\
# 					IPA:'kʰa3'\
# 				},\
# 				{	Num:'Zhang_VT_002',\
# 					Word:'(肉)羹',\
# 					IPA:'kĩ1'\
# 				},\
# 				{	Num:'Zhang_VT_003',\
# 					Word:'富(人)',\
# 					IPA:'pu5'\
# 				},\
# 				{	Num:'Zhang_VT_004',\
# 					Word:'(醫)治',\
# 					IPA:'ti6'\
# 				},\
# 				{	Num:'Zhang_VT_005',\
# 					Word:'(乖)巧',\
# 					IPA:'kʰa3'\
# 				}\
# 			]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 	
# 	
# 	def test_單詞短有誤(self):
# 		問題 = [
# 				['Num','Word','IPA check','Note'],
# 				['Zhang_VT_001','(乖)巧'	, 'kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題) 
# 		self.assertEqual(答案, 結果)
# 	
# 	
# 	def test_單詞短有誤2(self):
# 		問題 = [
# 				['Num','Word','IPA','Tone'],
# 				['Zhang_VT_001','(乖)巧'	, 'kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題) 
# 		self.assertEqual(答案, 結果)
# 	
# 	
# 	def test_單詞沒有開頭(self):
# 		問題 = [['Zhang_VT_001','(乖)巧', 'kʰa3','kʰa3']]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 		
# 	def test_單詞沒有開頭2(self):
# 		問題 = [
# 				['Num'],
# 				['Zhang_VT_001','(乖)巧', 'kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題) 
# 		self.assertEqual(答案, 結果)
# 		
# 		
# 	def test_單詞沒有開頭3(self):
# 		問題 = [
# 				['','Word'],
# 				['Zhang_VT_001','(乖)巧', 'kʰa3','kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 	
# 	
# 	def test_單詞沒有開頭4(self):
# 		問題 = [
# 				['','','IPA'],
# 				['Zhang_VT_001','(乖)巧', 'kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 			
# 			
# 	def test_位置錯換(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['(乖)巧','Zhang_VT_001', 'kʰa3']
# 			]
# 		答案 =  "[{Num:'Zhang_VT_001',\
# 				Word:'(乖)巧',\
# 				IPA:'kʰa3'\
# 				}]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 		
# 	def test_單詞資料有缺(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['','(乖)巧', 'kʰa3']
# 			]
# 		答案 =  "col(1)沒有編號"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 			
# 			
# 	def test_單詞資料有缺2(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Zhang_VT_001','', 'kʰa3']
# 			]
# 		答案 =  "col(1)沒有字"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 	
# 	
# 	def test_單詞資料有缺3(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Zhang_VT_001','(乖)巧', '']
# 			]
# 		答案 =  "col(1)沒有IPA"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 					
# 	def test_單詞沒括號(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Zhang_VT_001','乖巧', 'kʰa3']
# 			]
# 		答案 =  "col(1)的字不是單詞"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 					
# # 		雙詞
# 	def test_雙詞(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Rd001','市面', 'tsʰi4bin6']
# 			]
# 		答案 =  "[[Name:'Rd001', Word:'市面', IPA:'tsʰi4bin6']]"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 	def test_雙詞少個字(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Rd001','面', 'tsʰi4bin6']
# 			]
# 		答案 =  "col(1)少了字"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)
# 		
# 	def test_雙詞少個音(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Rd001','市面', 'bin6']
# 			]
# 		答案 =  "col(1)少了音"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)	
# 	
# 	def test_雙詞的音有誤(self):
# 		問題 = [
# 				['Name','Word','IPA'],
# 				['Rd001','市面', 'tsʰi4bin']
# 			]
# 		答案 =  "col(1)少了音"
# 		結果 = xlsx陣列轉json(問題)
# 		self.assertEqual(答案, 結果)	
# 	只有一個字
# IPA只有一個音
# IPA格式有誤 (這能檢查嗎?)
# 如果以後有三個音、四個音....??

if __name__=='__main__':
	unittest.main()