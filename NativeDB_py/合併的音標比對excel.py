from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
# import xlrd
# 先做完合併音節的位置.py
def 音標比對excel(xlsx檔名, 合併音標):
	excel音表 = 把EXCEL讀進來(xlsx檔名)
	# 1. 移掉表頭列 0th row = ['Num', 'Word', 'IPA', 'Note']
	excel音表.remove(excel音表[0])
	
	# 2. 音標合併第二次，以便和xlsx陣列作比較
	對應表 = []
	for 列 in 合併音標:
		對應表.append(''.join(列[0]))
		
	# 3. 紀錄沒有音檔或是可能標音錯誤的字
	# 合格的表：excel有對應到音檔，
	# 合格的字格：標音正確，有找到對應的excel
	合格的表 = []
	不合格的表 = []
	合格的字格 = []
	不合格的字格 = []
	
	# 	4. 先找出excel的詞當中，有哪些的IPA不在textgrid裡
	# 	順便紀錄合格的textgrid的索引，與合格的表的漢字和IPA
	for 列 in excel音表:
		if 列[2] in 對應表:
			# 	合格，因為在textgrid有對應音檔
			合格的字格.append(對應表.index(列[2]))
			合格的表.append(列[1:3])
		elif 列[3] == 'x':
			# 	合格，因為有紀錄此詞本身無對應音檔			
			pass
		else:
			# 	不合格
			不合格的表.append(列)
		
	# 	5. 檢查完excel後，也要挑出textgrid中沒有對應的IPA的，不合格的詞
	for 索引 in range(len(對應表)):
		if 索引 in 合格的字格:		
				pass
		else:
			不合格的字格.append(合併音標[索引])

	return 不合格的表, 不合格的字格, 合格的表