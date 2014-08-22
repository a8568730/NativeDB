from NativeDB_py.讀取EXCEL檔 import 把EXCEL讀進來
from NativeDB_py.把xlsx的陣列轉成json import xlsx陣列轉json
from NativeDB_py.寫出json檔 import 寫出json檔
import json


def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except:
		return False
	return True
 
 
excel檔名 = 'Penang_Y_M01_correct.xlsx'
xlsx陣列 = 把EXCEL讀進來(excel檔名)
if(len(xlsx陣列) != 0):
	json陣列 = xlsx陣列轉json(xlsx陣列, 1)
	if(type(json陣列[0]) is dict):
 		寫出json檔(json陣列, excel檔名)
# 	print(json陣列)
# 	result= json.loads("[{\"num\":\"100\"}]")
# 	print(result)
	else:
		# 輸出錯誤訊息		
		print(json陣列)	


