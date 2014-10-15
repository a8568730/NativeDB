import xlrd

def 把EXCEL讀進來(xlsx檔名):
	mybook = xlrd.open_workbook(xlsx檔名)
	
	寫出結果 = []
	
	# 	1. 為避免學姊的excel檔有太多雜頁，我們限制只能有一頁。
	if mybook.nsheets > 1:
		寫出結果='警告：excel檔的sheet超過一頁，請重新上傳'
	else:
		sheet0 = mybook.sheet_by_index(0)	
		# 	print(sheet0.row(0))
		# 	print(sheet0.cell_value(colx=0,rowx=0))
		# 	print(sheet0.row_values(0))
		for i in range(0, sheet0.nrows):
			寫出結果.append(sheet0.row_values(i))
			
	return 寫出結果	
