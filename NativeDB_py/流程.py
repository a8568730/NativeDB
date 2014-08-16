from NativeDB_py.取出聲音位置 import 取出聲音位置


資料 = 取出聲音位置('textgrid/Penang_M_M01_DiT.TextGrid')
寫出結果 = open('outputs/Penang_Y_M01_01.txt', 'w', encoding="utf-8")

for line in 資料:
 	print(line)