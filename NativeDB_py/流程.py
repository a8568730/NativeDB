from NativeDB_py.讀取TextGrid檔 import 讀取TextGrid檔
from NativeDB_py.檢查TextGrid和Wav名稱和總長度 import 檢查TextGrid和Wav名稱和總長度
from NativeDB_py.合併TextGrid的CVC時間 import 合併TextGrid的CVC時間
from NativeDB_py.照位置切割音檔 import 切割音檔
from NativeDB_py.檢查TextGrid合併CVC後的時間 import 檢查TextGrid合併CVC後的時間

# 	單詞：
# 文字檔路徑 = 'C:\\Users\\SIDK\\Desktop\\Penang_Y_M01_02.TextGrid'
# 聲音檔路徑 = 'C:\\Users\\SIDK\\Desktop\\Penang_Y_M01_02.wav'
文字檔路徑 = '/home/sui2/桌面/Penang_Y_M01_02.TextGrid'
聲音檔路徑 = '/home/sui2/桌面/Penang_Y_M01_02.wav'
# 	雙詞：


資料 = 讀取TextGrid檔(文字檔路徑)

檢查輸入字串 = 檢查TextGrid和Wav名稱和總長度(聲音檔路徑, 文字檔路徑, 資料[-1][-1])

if(檢查輸入字串 == 'OK'):
	#合併出每一個詞的頭尾時間
	合併後的資料 = 合併TextGrid的CVC時間(資料)
	檢查大小字串 = 檢查TextGrid合併CVC後的時間(合併後的資料)
	if(檢查大小字串 == 'OK'):
		#照每一個詞的頭尾時間去切割音檔
		切割音檔(聲音檔路徑, 合併後的資料)