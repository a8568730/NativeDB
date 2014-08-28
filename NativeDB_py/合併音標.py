import re

def 合併音標(合併後的資料):
	寫出結果 = []  
	# 	合併後的資料來自textGrid，	可能一口氣講了很多詞，一個詞可能是單字，雙字，三字，...
	for 一個詞的音標時間 in 合併後的資料:
		一個詞的音標陣列 = 一個詞的音標時間[0]

		暫存音標陣列 = []
		送出音標陣列 = [] 
		前一個純音素 = None
		前一個索引 = -1
		# 		一個詞所含的字(單字，	雙字，...)的音標串連，CVCVCV....
		for 音標 in 一個詞的音標陣列:
			#		格式 C1/V1-abcdz-1
			拆開減號後的音標 = re.split('-',音標)
			拆開括號後的音標 = re.split('(\(.*?\))',拆開減號後的音標[1]) 
			#		求目前括號外的這個音素，待會要找出現在此音素的索引，以便知道前後組音素是否來自同一字(CV)。
			for 音素 in 拆開括號後的音標:
				if(not '(' in 音素 and len(音素)>0):
					括號外的音 = 音素 
					break	
			
			#	算出實際上的完整音標，如果完整音標是一樣的就表示前後音素可能來自同一個字
			#	為了避免疊字詞，所以若是完整音標和音素索引都相同，就表示是疊字的同一位置
			純音素 = re.sub('[()]','',拆開減號後的音標[1])
			括號外的音的索引 = 純音素.index(括號外的音)
			# 	可能同種字
			if( 純音素 == 前一個純音素 ):
				# 	同種字但位置相同或是前者較大，估計前者是前一疊字的結尾
				if(前一個索引 >= 括號外的音的索引):
					送出音標陣列.append(前一個純音素)
			elif( 純音素 != 前一個純音素 and 前一個純音素 != None):
				送出音標陣列.append(前一個純音素)
			前一個純音素 = 純音素 
			前一個索引 = 括號外的音的索引
			
		# 		跳出迴圈後，處理最後一個字	
		送出音標陣列.append(前一個純音素)	
		寫出結果.append((送出音標陣列 ,一個詞的音標時間[1], 一個詞的音標時間[2])) 
		print(寫出結果)
		
	return 寫出結果 	