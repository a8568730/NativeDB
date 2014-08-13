
def 取出聲音位置(檔名):
	切割檔 = open(檔名, encoding="utf-8")
	資料 = 切割檔.readlines()
	切割檔.close()
	
	寫出結果 = []
	
	# 889 from "intervals: size = 889"
	區間數 = 資料[13].split(' ')[-2]
	有用的陣列範圍 = 14 + int(區間數) * 4
	
	# for 行1 in 資料[15:有用的陣列範圍]:
	# 	 行2 = 資料.next()
	# 	 print(行1, 行2, file=寫出結果)
	
	# XXX-C-V-XXX
	xmin = 0
	xmax = 0
	for 行 in 資料[14:有用的陣列範圍]:
		行陣列 = 行.split()
		print(行陣列)
		if(行陣列[0] == 'xmin'):
			xmin = 行陣列[2]
		elif(行陣列[0] == 'xmax'):
			xmax = 行陣列[2]
		elif(行陣列[0] == 'text'):
			寫出結果.append((行陣列[2].strip('"'), xmin, xmax))
# 			print(行陣列[2], xmin, xmax, file=寫出結果)
	return 	寫出結果		
	# 	 print(索引 ,行, file=寫出結果)
	
