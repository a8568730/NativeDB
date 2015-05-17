import xlrd
import math

def 讀取Excel檔(xlsx檔名):
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
			一列 = []
			for j in range(0, sheet0.ncols):
				儲存格類型 = sheet0.cell_type(i, j)
				儲存格值 = sheet0.cell_value(i, j)
				# 如果類型是Number，而且值是8.00，就要截掉後面的零
				if 儲存格類型 == 2 and math.modf(儲存格值)[0] == 0:
					儲存格值 = str(int(儲存格值))
				elif 儲存格類型 == 2:
					儲存格值 = str(儲存格值)	
				一列.append(儲存格值)	
			寫出結果.append(一列)
			
	return 寫出結果	
