
def 合併位置(資料):
	#	看到第一個xxx時, 下一行C的值要記錄min
	#	直到看到第二個xxx, 最後一行的值要紀錄max
	
	xxx	= 0
	sylmin = 1000000.0
	sylmax = -100.0
	syl = []
	寫出結果 = []
	for	line in 資料:
		名字,	xmin, xmax = line
		xmin = float(xmin)
		xmax = float(xmax)
		if(名字=="XXX" and xxx==0):
			xxx = 1
		elif(名字=="XXX" and xxx==1):
			寫出結果.append((','.join(syl), sylmin, sylmax))
			syl = []
		else:
			sylmin = xmin if sylmin > xmin else sylmin;
			sylmax = xmax if sylmax < xmax else sylmax;
			syl.append(名字)
	return 寫出結果		