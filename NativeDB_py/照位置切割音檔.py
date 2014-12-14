import wave
import io

#被切音檔路徑 MEDIA_ROOT/Penang1.wav
#被切音檔路徑 MEDIA_ROOT/漢字_Penang1.wav

def 切割音檔(被切音檔路徑, 完成音檔指標, 開頭時間, 結尾時間):
# 	合併後的資料，可能好幾組文字的切割時間區間
# 	[(字1, '開頭', '結尾'), ...]
	
	origAudio = wave.open(被切音檔路徑,'r')
	frameRate = origAudio.getframerate()
	nChannels = origAudio.getnchannels()
	sampWidth = origAudio.getsampwidth()
	nFrames = origAudio.getnframes()
	
	# 	0.2和0.1是隨便給的
	start = int((float(開頭時間) - 0.05)*frameRate)
	end = int((float(結尾時間) + 0.01)*frameRate)
	
	# 	若是輸入的切割位置超出了音檔的長度，就切齊。
	if(start < 0):
		start = 0
	if(end > nFrames):
		end = nFrames		
	anchor = origAudio.tell()
	origAudio.setpos(anchor + start)
	chunkData = origAudio.readframes(end-start)
		
	#	分為切割一次或兩次以上的檔名取法
# 		if(切割總數 > 1):
# 			輸出名 = 音檔原名 + '_chunk.wav' 
# 		else:
# 			輸出名 = 音檔原名 + '_chunk.wav'
	chunkAudio = wave.open(完成音檔指標,'w')
	chunkAudio.setnchannels(nChannels)
	chunkAudio.setsampwidth(sampWidth)
	chunkAudio.setframerate(frameRate)
	chunkAudio.writeframes(chunkData)
	
	chunkAudio.close()
	origAudio.close()
	