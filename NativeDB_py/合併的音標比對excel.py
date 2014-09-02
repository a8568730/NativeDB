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
	有存在音檔的字陣列 = []
	合格的表 = []
	不合格的表 = []
	
	for 表索引, 列 in enumerate(excel音表):
		if (列[2] in 對應表):
			文格索引 = 對應表.index(列[2])
			有存在音檔的字陣列.append((表索引, 文格索引))
		else:
			列[3] = 'x'
			不合格的表.append(列)
	for 表索引, 列 in enumerate(excel音表):
		if (表索引 in 合格的表):
			文格索引 = 對應表.index(列[2])
			有存在音檔的字陣列.append((表索引, 文格索引))
		else:
			列[3] = 'x'
			不合格的表.append(列)
			
	for 數對 in 有存在音檔的字陣列:
		excel音表.remove(數對[0])
		合併音標.remove(數對[1])
	
	if (len(excel音表) > 0 or len(合併音標) > 0 ):
		print('Excel 沒有音檔的{0}\nTextGrid中沒有對應的IPA{1}'.format(excel音表,合併音標))
		return False
	else:
		return True
