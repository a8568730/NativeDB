import re
# 	合併後的資料來自textGrid

# 桌桌  [(['C1-t(oʔ8)-1', 'V1-(t)o(ʔ8)-1', 'C1-(to)ʔ(8)-1', 'C1-t(oʔ8)-1', 'V1-(t)o(ʔ8)-1', 'C1-(to)ʔ(8)-1'], '1.5', '1.8')]
# 1. 取得['C1-t(oʔ8)-1', 'V1-(t)o(ʔ8)-1', 'C1-(to)ʔ(8)-1', 'C1-t(oʔ8)-1', 'V1-(t)o(ʔ8)-1', 'C1-(to)ʔ(8)-1']
# 2. 拆開括號後 
# 桌 [t, (oʔ8)],  [(t), o, (ʔ8)],  [(to), ʔ, (8)] 
# 桌 [t, (oʔ8)],  [(t), o, (ʔ8)],  [(to), ʔ, (8)]         
# 2. 拆開括號後算索引 
# 桌 [t, (oʔ8)],  [(t), o, (ʔ8)],  [(to), ʔ, (8)] =>  0, 1, 2
# 桌 [t, (oʔ8)],  [(t), o, (ʔ8)],  [(to), ʔ, (8)] =>  0, 1, 2   
# 同一字的索引是遞增的，於是可以知道疊字詞的斷點 

def 合併音標(合併後的資料):
	寫出結果 = []  
	for 一個詞的音標時間 in 合併後的資料:
		# 1. 
		一個詞的音標陣列 = 一個詞的音標時間[0]

		# 2. 
		送出音標陣列 = [] 
		前一個純音素 = None
		前一個索引 = -1
		
		for 音標 in 一個詞的音標陣列:
			拆開減號後的音標 = re.split('-',音標)
			拆開括號後的音標 = re.split('(\(.*?\))',拆開減號後的音標[1]) 
			#	2a. 目前的音素特徵是無括號，求出它在完整音標的索引
			累積的音標 = ''
			for 音素 in 拆開括號後的音標:
				if len(音素) ==0:
					pass
				elif '(' in 音素: 
					累積的音標 += re.sub('[()]','',音素)
				else:
					括號外的音的索引 = len(累積的音標)
					break	
			
			
			#	純音素：實際上的完整音標，如果完整音標是一樣的代表前後音素可能來自同一個字的C或V，或是疊字 
			#	括號外的音的索引：為了避免疊字詞，當完整音標相同，可用音素索引判斷疊字的斷點
			純音素 = re.sub('[()]','',拆開減號後的音標[1])
						
			# 	同字，或疊字
			if( 純音素 == 前一個純音素 ):
				# 	同字但前一個括號外的音的索引較大或相同，估計前者是前一疊字的結尾
				if(前一個索引 >= 括號外的音的索引):
					送出音標陣列.append(前一個純音素)
			elif( 純音素 != 前一個純音素 and 前一個純音素 != None):
				送出音標陣列.append(前一個純音素)
			前一個純音素 = 純音素 
			前一個索引 = 括號外的音的索引
			
		# 		跳出迴圈後，處理最後一個字	
		送出音標陣列.append(前一個純音素)	
		寫出結果.append((送出音標陣列 ,一個詞的音標時間[1], 一個詞的音標時間[2])) 
		
	return 寫出結果 	