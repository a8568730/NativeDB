import json
import os


def 寫出json檔(json陣列, 參考用的excel檔名):
	輸出檔名 = os.path.splitext(參考用的excel檔名)[0] + '.json'
	
	with open(輸出檔名, 'w') as outfile:
		json.dump(json陣列, outfile, ensure_ascii=False)
	
	#	附註：後面的參數的意義。ensure_ascii 預設為True, 所有非ASCII的字會變成\uXXXX樣子。
	# 	就不能正常顯示IPA。