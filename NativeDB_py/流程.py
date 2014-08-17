from NativeDB_py.取出聲音位置 import 取出聲音位置
from NativeDB_py.合併音節的位置 import 合併位置
from NativeDB_py.照位置切割音檔 import 切割音檔

資料 = 取出聲音位置('textgrid/Penang_Y_M01_01.TextGrid')

# for line in 資料:
#  	print(line)
合併後的資料 = 合併位置(資料)

print(合併後的資料)

切割音檔('C:\\Users\\一生懸命是我的任俠道\\Desktop\\Penang_Y_M01_01.wav', 合併後的資料)