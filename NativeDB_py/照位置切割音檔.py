import wave
import os


def 切割音檔(音檔路徑, 合併後的資料):
# 	合併後的資料，可能好幾組文字的切割時間區間
# 	[(字1, '開頭', '結尾'), ...]
	for 一筆資料 in 合併後的資料:
		origAudio = wave.open(音檔路徑,'r')
		frameRate = origAudio.getframerate()
		nChannels = origAudio.getnchannels()
		sampWidth = origAudio.getsampwidth()
		start = float(一筆資料[1]) - 0.2
		end = float(一筆資料[2]) + 0.1

		anchor = origAudio.tell()
		origAudio.setpos(anchor + int(start*frameRate))
		chunkData = origAudio.readframes(int((end-start)*frameRate))
		
		
		音檔原名 = os.path.splitext(音檔路徑)[0]
		輸出名 = 音檔原名 + '_chunk.wav' 
		chunkAudio = wave.open(輸出名,'w')
		chunkAudio.setnchannels(nChannels)
		chunkAudio.setsampwidth(sampWidth)
		chunkAudio.setframerate(frameRate)
		chunkAudio.writeframes(chunkData)
		
		chunkAudio.close()
		origAudio.close()

		