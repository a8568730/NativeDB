from NativeDB_py.合併的音標比對excel import 音標比對excel

def 檢查不合格的表與字格(xlsx檔名, 合併音標):
	不合格的表, 不合格的字格, 合格的表 = 音標比對excel(xlsx檔名, 合併音標)
	
	if not len(不合格的表) == 0 or not len(不合格的字格) == 0:
		print('找不到對應的textgrid的EXCEL字：有{0}個\n找不到對應的IPA的Textgrid：有{1}個\n'.format(len(不合格的表), len(不合格的字格)))
		raise RuntimeError(不合格的表, 不合格的字格)

# 用在切割音檔後，建立傳好的表的IPA欄位與漢字欄位
def 輸出合格的表(xlsx檔名, 合併音標):
	不合格的表, 不合格的字格, 合格的表 = 音標比對excel(xlsx檔名, 合併音標)
	return 合格的表