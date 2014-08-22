import json

def 寫出json檔(json陣列, 輸出檔名):
	with open(輸出檔名, 'w') as outfile:
		json.dump(json陣列, outfile)