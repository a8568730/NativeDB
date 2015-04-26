import urllib.request


if __name__ =='__main__':
	for i in range (1,256):
		print(i)
		try:
			資料=urllib.request.urlopen("http://140.114.116.{}".format(i),timeout=3).read().decode('utf-8')
# 			print(資料)
			if '海外'  in 資料:
				print(i,'ok')
		except:
			pass