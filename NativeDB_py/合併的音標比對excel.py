from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
# import xlrd

def 音標比對excel(xlsx檔名,  合併音標):
	excel音表 = 把EXCEL讀進來(xlsx檔名)
	# 移掉表頭列 0th row = ['Num', 'Word', 'IPA', 'Note']
	excel音表.remove(excel音表[0])
	
	# 音標合併第二次，以便和xlsx陣列作比較
	對應表 = []
	for 列 in 合併音標:
		對應表.append(''.join(列[0]))
		
	# 紀錄沒有音檔或是可能標音錯誤的字
# 	有存在音檔的字陣列 = []
	合格的表 = []
	不合格的表 = []
	合格的字格 = []
	不合格的字格 = []
	
	for 列 in excel音表:
		if 列[2] in 對應表:
			# 	合格
			合格的字格.append( 對應表.index(列[2]) )
		elif 列[3] == 'x':
			# 	合格			
			pass
		else:
			# 	不合格
			不合格的表.append(列)
		
	# 	檢查完excel後，也順便找出textgrid中無法對應的元素
	for 索引 in range(len(對應表)):
		if 索引 in 合格的字格:		
				pass
		else:
			不合格的字格.append(合併音標[索引])

	if not len(不合格的表) == 0:
		print('Excel 中沒有音檔的: {0}'.format(不合格的表))
		if not len(不合格的字格) == 0:
			print('TextGrid中沒有對應的IPA: {0}'.format(不合格的字格))
		return False
	else:
		return True
