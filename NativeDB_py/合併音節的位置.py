

fp = open('outputs/Penang_Y_M01_01.txt',	encoding='utf-8')


#	看到第一個xxx時, 下一行C的值要記錄min
#	直到看到第二個xxx, 最後一行的值要紀錄max

xxx	= 0
sylmin = 1000000.0
sylmax = -100.0
syl = []
for	line in fp:
	名字,	xmin, xmax = line.strip().split(' ')
	xmin = float(xmin)
	xmax = float(xmax)
	if(名字=="XXX" and xxx==0):
		xxx = 1
	elif(名字=="XXX" and xxx==1):
		print(','.join(syl), sylmin, sylmax)
		syl = []
	else:
		sylmin = xmin if sylmin > xmin else sylmin;
		sylmax = xmax if sylmax < xmax else sylmax;
		syl.append(名字)
