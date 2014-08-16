from NativeDB_py.取出聲音位置 import 取出聲音位置
from NativeDB_py.合併音節的位置 import 合併位置

資料 = 取出聲音位置('textgrid/Penang_M_M01_DiT.TextGrid')

# for line in 資料:
#  	print(line)
合併後的資料 = 合併位置(資料)