import wave
import os


def 切割音檔(音檔路徑, 合併後的資料):
# 	合併後的資料，可能好幾組文字的切割時間區間
# 	[(字1, '開頭', '結尾'), ...]
	音檔原名 = os.path.splitext(音檔路徑)[0]
	
	for 第幾筆, 一筆資料 in enumerate(合併後的資料):
		origAudio = wave.open(音檔路徑,'r')
		frameRate = origAudio.getframerate()
		nChannels = origAudio.getnchannels()
		sampWidth = origAudio.getsampwidth()
		nFrames = origAudio.getnframes()
		
		# 	0.2和0.1是隨便給的
		start = int((float(一筆資料[1]) - 0.05)*frameRate)
		end = int((float(一筆資料[2]) + 0.01)*frameRate)
		
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
		輸出名 = 音檔原名 + '_' + ("{0:05d}").format(第幾筆+1) +'.wav'
			
		chunkAudio = wave.open(輸出名,'w')
		chunkAudio.setnchannels(nChannels)
		chunkAudio.setsampwidth(sampWidth)
		chunkAudio.setframerate(frameRate)
		chunkAudio.writeframes(chunkData)
		
		chunkAudio.close()
		origAudio.close()
