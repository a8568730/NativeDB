import re

def xlsx陣列轉json(xlsx陣列, 詞數):
	寫出結果 = []

# 	是否剛好有四個欄位
	欄數=len(xlsx陣列[0])
	print(xlsx陣列[0])
	if(欄數!=4):
		return 'xlsx檔要四個欄位: Num, Word, IPA, Note'

# 	第一行是否為這四個欄位:'Num','Word','IPA', Note
	預期欄位 = ["Num","Word","IPA", "Note"]
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

		#	編號的頭尾去掉數字、得到編號名稱 		
		編號字 = 完整編號.strip('0123456789')
		if(編號字 != 初始編號字):
			return 'col(' + str(索引+1) + ')的Num有誤'
		
		#	字不能為空字串
		if(len(字)==0):
			return 'col(' + str(索引+1) + ')的Word欄位空白'
		
		#	字不能有其他奇怪符號
		if(any(c in 字 for c in ' *$&#^%@~+|,.')):
			return 'col(' + str(索引+1) + ')含特殊符號'
		
		
		#	若是單詞卻有兩字以上, 雙詞卻有三字以上, 必須有括號
		if(詞數 != len(字)):
			regex = re.compile('\(.*?\)')
			去掉括號後的字們 = regex.sub(',', 字)

			
			if(去掉括號後的字們==''):
				return 'col(' + str(索引+1) + ')的字格式不符'
			
			括號外的字陣列 = 去掉括號後的字們.split(',')
			有符合詞數 = False
			for 一個 in 括號外的字陣列:
				if(len(一個) == 詞數):
					有符合詞數  = True
			
			if(not 有符合詞數):
				return 'col(' + str(索引+1) + ')的字格式不符'
		
		#	IPA不能為空字串
		if(len(音標)==0):
			return 'col(' + str(索引+1) + ')的IPA欄位空白'
		
		寫出結果.append(
				{預期欄位[0]: 編號字 + ("{0:0"+str(初始編號數字長度)+"d}").format(索引+1),
				預期欄位[1]: 字, 
				預期欄位[2]: 音標,
				預期欄位[3]:註記
			});	
# 	return 'OK'
	return 寫出結果
