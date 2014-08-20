import re

def xlsx陣列轉json(xlsx陣列, 詞數):
	寫出結果 = []

# 	是否剛好有四個欄位
	欄數=len(xlsx陣列[0])
	if(欄數!=4):
		return 'xlsx檔要四個欄位: Num, Word, IPA, Note'

# 	第一行是否為這四個欄位:'Num','Word','IPA', Note
	預期欄位 = ['Num','Word','IPA', 'Note']
	for 索引 in range(欄數):
		if(xlsx陣列[0][索引] != 預期欄位[索引]):
			return 'col(1,' + str(索引) + ')應為' + 預期欄位[索引]
	
# 	從第二行開始讀每一組資料
	for 索引, 一組 in enumerate(xlsx陣列[1:]):
		[完整編號, 字, 音標, 註記] = 一組
		
		#	編號要一致
		if(索引 == 0):
			初始編號字 = 完整編號.strip('0123456789')
			初始編號數 = re.sub(初始編號字, '', 完整編號)
			初始編號數字長度 = len(初始編號數)

		編號字 = 完整編號.strip('0123456789')
		if(編號字 != 初始編號字):
			return 'col(' + str(索引+1) + ')的Num有誤'
		
		#	字不能為空字串
		if(len(字)==0):
			return 'col(' + str(索引+1) + ')沒有字'
		
		#	字不能有其他奇怪符號
		if(any(c in 字 for c in '*$&#^%@~+|')):
			return 'col(' + str(索引+1) + ')含特殊符號'
		
		#	不能只有括號
		if('()' == 字):
			return 'col(' + str(索引+1) + ')只有()'
		
		patternL = re.compile(r'[\u4e00-\u9fff]{'+ str(詞數) +'}(\([\u4e00-\u9fff]*\))')
		patternR = re.compile(r'[\([\u4e00-\u9fff]*\)][\u4e00-\u9fff]{'+ str(詞數) +'}')
		patternP = re.compile(r'[\u4e00-\u9fff]{'+ str(詞數) +'}')
		if((not patternL.fullmatch(字)) or (not patternR.fullmatch(字)) or (not patternP.fullmatch(字))):
			return 'col(' + str(索引+1) + ')的字格式不符'
		
		#	若是單詞卻有兩字以上, 雙詞卻有三字以上, 必須有括號
		if(詞數 != len(字)):
			括號組="()"
			for 括號 in 括號組:
				if(字.find(括號)==-1):
					return 'col(' + str(索引+1) + ')的Word少了' + 括號 
			
			#	()以外的字不得少於詞數
			第一次切出, 剩餘字串 = 字.split('(')
			括號內的字串, 第二次切出 = 剩餘字串.split(')') 
			if(len(第一次切出) != 詞數 and len(第二次切出) != 詞數):
				return 'col(' + str(索引+1) + ')的Word字數應為' + str(詞數)
			
	return 'OK'

