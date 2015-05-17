from NativeDB_py.讀取Excel檔 import 讀取Excel檔
from NativeDB_py.檢查Excel檔格式與內容 import 檢查Excel檔格式與內容

excel檔名 = 'numberbook2.xlsx'
xlsx陣列 = 讀取Excel檔(excel檔名)

# 輸出sheet超過一頁的錯誤訊息
if isinstance(xlsx陣列, str):
	print(xlsx陣列)
	
elif(len(xlsx陣列) != 0):
	json陣列 = 檢查Excel檔格式與內容(xlsx陣列, 1)
	if(type(json陣列[0]) is dict):
		print('success', json陣列)
	else:	
		# 輸出錯誤訊息
		print('ohno', json陣列)
