import xlrd

def 把EXCEL讀進來(xlsx檔名):
	mybook = xlrd.open_workbook(xlsx檔名)
	sheet0 = mybook.sheet_by_index(0)
	寫出結果 = []
	
# 	print(sheet0.row(0))
# 	print(sheet0.cell_value(colx=0,rowx=0))
# 	print(sheet0.row_values(0))

	for i in range(0, sheet0.nrows):
		寫出結果.append(sheet0.row_values(i))
	return 寫出結果	
