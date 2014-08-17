#	wav、textgrid
#	檔案名稱要一致。
# 	時間長度要一樣。
import os
import wave

def 檢查輸入(音檔完整路徑, 文字格完整路徑, 文字檔秒數):
	
# 	檢查檔名, 會先去掉副檔名
	音檔名 =  os.path.basename(os.path.splitext(音檔完整路徑)[0])
	文字格名 = os.path.basename(os.path.splitext(文字格完整路徑)[0])
	
	if 音檔名 != 文字格名:
		return 'wav和textGrid的檔名不一致'
		
# 	檢查長度
	origAudio = wave.open(音檔完整路徑,'r')
	frameRate = origAudio.getframerate()
	samplenum = origAudio.getnframes() 
	origAudio.close()
	
	文字檔看到的點數 = float(文字檔秒數)*frameRate
	
	if 文字檔看到的點數 > samplenum:
		return 'textGrid比wav的時間還長，可能不是同一組'
	elif abs(文字檔看到的點數 - samplenum) > frameRate:
		return 'wav和textGrid的長度差太多，可能不是同一組'
			
	return 'OK'	