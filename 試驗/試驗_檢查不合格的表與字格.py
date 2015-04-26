import unittest
import os
from NativeDB_py.合併音標比對excel結果 import 檢查不合格的表與字格
from NativeDB_py.合併的音標比對excel import 音標比對excel


class 基本元素試驗(unittest.TestCase):
	def setUp(self):
		self.檔案所在 = os.path.join(os.path.dirname(__file__),'..','NativeDB_py')
	def tearDown(self):
		pass
	
	def test_比對_桌1(self):
		檔案 =  os.path.join(self.檔案所在 ,'numberbook1.xlsx')
		問題 = [(['toʔ8'], '1.7946093688657765', '2.02')]
		答案 = None
		結果 = 檢查不合格的表與字格(檔案, 問題)
		self.assertEqual(答案, 結果)
		
	def test_比對_記者交保以前(self):
		檔案 = os.path.join(self.檔案所在 ,'numberbook3.xlsx')
		問題 = [(['ki5', 'tsia3'], '1.7946093688657765', '2.02'), (['kau1', 'po3'], '4.38', '7.7')]
		self.assertRaises(RuntimeError, 檢查不合格的表與字格, 檔案, 問題)
	
	def test_比對_雞婆(self):
		檔案 = os.path.join(self.檔案所在 ,'numberbook4.xlsx')
		問題 = [(['ke1', 'po2'], '1.7946093688657765', '7.7')]
		self.assertRaises(RuntimeError, 檢查不合格的表與字格, 檔案, 問題)
		
	def test_比對_雙語(self):
		檔案 = os.path.join(self.檔案所在 ,'Penang_DiT_M_M01.xlsx')
		問題 = [(['keʔ9', ' piaʔ7'], '14.740574729819627', '15.075353933741027'),
					 (['hu2', ' kut7'], '18.77385414161029', '19.26625697137455'),
					 (['put7', ' si2'], '28.815642190509244', '29.271843682035016'),
					 (['kɔ1', ' so3'], '33.63810246089005', '34.11550322470964'),
					 (['taʔ9', ' pɔ5'], '44.99102428536262', '45.4476806663668'),
					 (['te6', ' tɔ2'], '49.295624723288405', '49.75721781203228'),
					 (['ko1', ' kip7'], '53.48328596126247', '53.845303513596484'),
					 (['keʔ7', ' paʔ7'], '64.3107333966327', '64.65126500530717'),
					 (['pueʔ9', ' ki1'], '68.44052622506138', '68.91486954446293'),
					 (['tsʰi4', ' ke5'], '73.38725533052218', '73.97269770352064'),
					 (['tui3', ' tsiʔ7'], '86.75663471321866', '87.1205208425927'),
					 (['pai2', ' tui6'], '90.63469725843467', '91.18589496350492'),
					 (['pɔ6', ' sɔ5'], '95.1412645046806', '95.63189831000534'),
					 (['tioʔ0', ' kip7'], '125.89746766003162', '126.21912104742034'),
					 (['to6', ' tik7'], '130.0072267379865', '130.33456116518144'),
					 (['pɔ3', ' sip8'], '133.77865877240194', '134.15179971737172'),
					 (['tsioʔ0', ' hut8'], '137.99877981185537', '138.4118052328583'),
					 (['to4', ' kɛ1'], '142.2470076170122', '142.71355864779437'),
					 (['po5', ' kɔk7'], '152.75715824731068', '153.11137793225308'),
					 (['peʔ0', ' peʔ8'], '156.85120370041216', '157.27561412352276'),
					 (['to6', ' kau5'], '161.3050550242606', '161.7620442092189'),
					 (['tiʔ9', ' hɔ6'], '165.45284019717852', '165.92391583197167'),
					 (['kɔ1', ' po2'], '169.54616681235345', '170.02319491007978'),
					 (['to6', ' ka1'], '174.13014740867982', '174.58554717965876'),
					 (['tui5', ' ku5'], '184.55278358485714', '185.02357704863195'),
					 (['be4', ' tsʰi5'], '188.9110828308377', '189.44525845626603'),
					 (['tui5', ' tik8'], '193.51239677342622', '193.90101030915488'),
					 (['pueʔ9', ' pai2'], '205.61684363195172', '206.12562424968297'),
					 (['pɔ5', ' si2'], '210.27336142701233', '210.83830651611444'),
					 (['te6', ' tsap8'], '214.77944444965354', '215.15598563300685'),
					 (['si2', ' kiɔk8'], '219.11430308561094', '219.64337340337062'),
					 (['huat7', ' kut8'], '233.76359947753613', '234.25650032442988'),
					 (['be4', ' tok8'], '239.9182572382746', '240.33955908222154'),
					 (['po3', ' hu6'], '244.9596979177678', '245.43301865727216'),
					 (['te6', ' si5'], '255.40950817318867', '256.01253233860274'),
					 (['pui2', ' tu1'], '260.4503542149177', '260.88912151481605'),
					 (['be4', ' tsua3'], '265.8163299661602', '266.4017110338467'),
					 (['tsiaʔ0', ' tse6'], '270.4529640420197', '271.0504964102799'),
					 (['peʔ0', ' tau6'], '279.563183316865', '280.08763150583616'),
					 (['sia7', ' ke5'], '288.00558294830546', '288.65504822028004'),
					 (['ku4', ' koŋ1'], '297.5583501732301', '298.03578887792474'),
					 (['kut8', ' to3'], '308.0850974151279', '308.5722942477209'),
					 (['ka5', ' sai3'], '337.7598312408766', '338.33862008449756'),
					 (['kuaʔ9', ' hue5'], '347.48640098869345', '348.0566193281041'),
					 (['si2', ' ki1'], '351.93086045992686', '352.51983094569226'),
					 (['paʔ9', ' kau3'], '356.6527244151442', '357.17030092830686'),
					 (['sit8', ' tue2'], '371.66191343466215', '372.2256327881944'),
					 (['to3', ' tai2'], '378.5753436758212', '379.1251285509606'),
					 (['go4', ' tsap8'], '383.28285509244273', '383.7033558872275'),
					 (['sit7', ' pue2'], '387.9676137987307', '388.5745937330376'),
					 (['tu1', ' tɔ6'], '393.17327268544545', '393.66799552332617'),
					 (['hau6', ' ko3'], '397.9437345052132', '398.53831553367763'),
					 (['ki2', ' to6'], '402.5951137535791', '403.1137821783606'),
					 (['tsiaʔ0', ' sɔ5'], '418.2366724657955', '418.86569743300333'),
					 (['po3', ' te6'], '466.79917446055043', '467.3652064760075'),
					 (['te2', ' pue1'], '471.0523865385348', '471.59027829357234'),
					 (['te6', ' kiu2'], '475.46315658286244', '475.92469827570034'),
					 (['siaʔ9', ' ʔioʔ8'], '479.771246644944', '480.28328864400066'),
					 (['kau3', ' tsioʔ0'], '484.39660952422565', '484.91410370018207'),
					 (['tsioʔ0', ' kau2'], '489.13749191786883', '489.7068989757583'),
					 (['tua6', ' tsiʔ8'], '493.3637550749509', '493.8899088665205'),
					 (['bi4', ' le6'], '498.0267531348147', '498.5444323746119'),
					 (['kɔk7', ' su6'], '502.75866057023285', '503.2476910535085'),
					 (['tsioʔ0', ' hioʔ8'], '510.5248951845705', '510.9896743484669'),
					 (['hut8', ' kau5'], '514.8830203117292', '515.4345868989424'),
					 (['paʔ9', ' ki2'], '519.3673721929092', '519.8991056897158'),
					 (['pai5', ' put8'], '523.6742010627787', '524.0423363138129'),
					 (['huat7', ' sut8'], '528.3235262759976', '528.8000518549775'),
					 (['peʔ0', ' pɔ5'], '542.6922242632211', '543.1734561044364'),
					 (['paʔ9', ' pɤ6'], '546.7358707505235', '547.2457491908243'),
					 (['put7', ' ko5'], '556.8593126497769', '557.2806370203554'),
					 (['ka6', ' to1'], '562.406655212877', '562.9734655959489'),
					 (['tsioʔ0', ' kɔ3'], '566.4974230317865', '567.0528603467054'),
					 (['peʔ0', ' to1'], '570.5857570976608', '571.095078809055'),
					 (['hak8', ' tsia3'], '575.9607147943105', '576.4954036191157'),
					 (['ko5', ' si2'], '582.5759287044209', '583.0834145955783'),
					 (['pak7', ' pɔ6'], '586.9754670263527', '587.4585670176534'),
					 (['hak8', ' hau6'], '591.3272805121518', '591.9150784413298'),
					 (['tɨ1', ' tsiʔ8'], '596.6242629187789', '597.1011643798852'),
					 (['po5', ' tsua3'], '600.9632018002978', '601.4799429505312'),
					 (['tsioʔ0', ' ko1'], '605.3472502004706', '605.9110000454394'),
					 (['siu1', ' pit7'], '610.0858506361236', '610.5667599017698'),
					 (['to4', ' kau5'], '615.1798538609656', '615.6532496801625'),
					 (['tsiaʔ0', ' te2'], '619.4733370765867', '619.9820501944339'),
					 (['po3', ' pi5'], '623.6570752024267', '624.1533050653184'),
					 (['tɔk8', ' kɔ1'], '628.5041780603405', '629.0132187654148'),
					 (['ʔi4', ' tsiəŋ2'], '633.1721904229801', '633.6601659938101'),
					 (['kuaʔ9', ' te5'], '639.548054310972', '640.0429483452327'),
					 (['tsap8', ' ki1'], '644.1005472820485', '644.573153448171'),
					 (['keʔ9', ' kiɔk8'], '648.8379843889783', '649.2120291716608'),
					 (['ki2', ' kuai5'], '660.8390893448351', '661.3184109050185'),
					 (['kiu2', ' toʔ7'], '668.8980054294228', '669.3455640406715'),
					 (['pueʔ9', ' so3'], '672.9551479262362', '673.460203547143'),
					 (['be4', ' hi2'], '677.0811984733317', '677.6576775913339'),
					 (['tsioʔ0', ' hɔ3'], '682.1409412596452', '682.6746187088077'),
					 (['tik8', ' piӕt8'], '686.5636558698341', '686.92191254279'),
					 (['tsap8', ' kau3'], '691.3033507336899', '691.8499501296527'),
					 (['paʔ7', ' kiok8'], '695.4778510110069', '695.8523392249789'),
					 (['piau1', ' ki6'], '700.1795388577691', '700.6920997583064'),
					 (['hap8', ' sip8'], '705.156620937327', '705.6121397686705'),
					 (['pueʔ9', ' ki2'], '710.2431391035764', '710.7138482217033'),
					 (['peʔ0', ' ki2'], '714.8512279830761', '715.3374138132738'),
					 (['tsi3', ' sɔ5'], '719.4254425638909', '719.9601915885022'),
					 (['kɔk7', ' po3'], '724.2395238120388', '724.7179042461506'),
					 (['be4', ' ki2'], '728.9813719164797', '729.4998361361204'),
					 (['hu2', ' ke5'], '733.9648892628604', '734.4883020158439'),
					 (['ki1', ' te6'], '738.8494879705794', '739.3455794472875'),
					 (['to4', ' tik7'], '750.5680888159026', '750.9338542722755'),
					 (['tua6', ' to1'], '755.4127960063431', '755.9350004920129'),
					 (['te6', ' pɔ6'], '760.1432800074217', '760.6756848175075'),
					 (['be4', ' tik7'], '765.5170942774505', '765.8591385631606'),
					 (['go4', ' tok8'], '775.1128114170614', '775.5286848345746'),
					 (['tsit7', ' pai3'], '783.8109660495544', '784.2698262053647'),
					 (['sit8', ' tsai6'], '788.0589909359004', '788.6175100734561'),
					 (['kue1', ' po2'], '800.7209039194078', '801.2007819178046'),
					 (['ka1', ' po3'], '805.4725935784446', '805.9785725172052'),
					 (['kɔ1', ' ki1'], '810.3393740305215', '810.8445036947799'),
					 (['hak8', ' ki2'], '814.7719748285308', '815.3076784168272'),
					 (['tsui3', ' sik7'], '820.1889911366789', '820.6646557367561'),
					 (['po3', ' to3'], '825.1509766646341', '825.6415519092092'),
					 (['pok7', ' kua5'], '835.1687777652974', '835.6122758544344'),
					 (['tsʰi4', ' bin6'], '840.5554065626824', '841.0795900064151'),
					 (['po3', ' to1'], '845.5141447512996', '846.026096759609'),
					 (['ho3', ' te2'], '850.0659913819857', '850.665191613189'),
					 (['tɔ2', ' tue6'], '855.2764730172378', '855.7821370559899'),
					 (['peʔ0', ' sik7'], '860.5813579683232', '860.9403573519172'),
					 (['hak8', ' si6'], '865.7406734036113', '866.2688110031347'),
					 (['kue5', ' tɔ6'], '872.1191717921001', '872.644187209126'),
					 (['hok8', ' ʔioʔ8'], '878.194158349375', '878.6579129860392'),
					 (['sit7', ' pai6'], '898.4083593539232', '899.0274997585636'),
					 (['be4', ' bi4'], '903.0771418050433', '903.6311679558069'),
					 (['hɔ6', ' tiʔ7'], '907.6619948692013', '908.2324815502009'),
					 (['tik7', ' kɔk7'], '911.9617739534575', '912.2739894144429'),
					 (['pue6', ' sik8'], '916.6576389240062', '917.0422481521016'),
					 (['tik8', ' ki1'], '922.0744367709352', '922.5427804277417'),
					 (['piau3', ' te6'], '938.4529334859488', '938.99784097578'),
					 (['pueʔ7', ' to6'], '943.2837326365517', '943.7793163570075'),
					 (['pai2', ' kut7'], '948.1352448128695', '948.5096892046113'),
					 (['kau6', ' kau6'], '965.9671499965149', '966.4664029642779'),
					 (['ʔioʔ0', ' tsui3'], '970.3768991916095', '970.8790711087263'),
					 (['pai2', ' tsui3'], '975.5757909880317', '976.0451884348446'),
					 (['tik8', ' kɔk7'], '980.7664832774267', '981.1084191990301'),
					 (['tik7', ' pak7'], '997.6620528559395', '998.0288269294889'),
					 (['ki2', ' ho6'], '1001.883810344865', '1002.3241961069305'),
					 (['pui2', ' hu2'], '1007.3343019844381', '1007.8308244362789'),
					 (['tsok7', ' ho3'], '1013.2531724192727', '1013.7727319842563'),
					 (['tok8', ' ke5'], '1023.9000646951343', '1024.3600935938302'),
					 (['tsit8', ' tiʔ7'], '1028.6685723191993', '1029.0743936284618'),
					 (['kau5', ' su1'], '1045.8308642826296', '1046.3724560671317'),
					 (['kai3', ' kuat8'], '1050.8985487285488', '1051.239614777994'),
					 (['pai5', ' si5'], '1055.4991720908502', '1056.0113501559429'),
					 (['hap8', ' si2'], '1060.010012149849', '1060.5409266774868'),
					 (['pueʔ9', ' ho6'], '1064.8139562579381', '1065.2642405145468'),
					 (['pɔ5', ' te6'], '1069.9634008501828', '1070.4849242090215'),
					 (['po5', ' kɛ5'], '1074.3260050706838', '1074.8276552233865'),
					 (['peʔ0', ' tu1'], '1079.0699317456622', '1079.5631256116185'),
					 (['pau1', ' su1'], '1083.550473069768', '1084.0882524837969'),
					 (['hɯ2', ' ti2'], '1106.52979327316', '1107.0694426718426'),
					 (['kɔ5', ' kau1'], '1111.3559061520098', '1111.9306809500692'),
					 (['te6', ' kau3'], '1115.678020663627', '1116.1896889503034'),
					 (['kue5', ' ki2'], '1120.5801918487223', '1121.0683213210946'),
					 (['ki2', ' sit8'], '1124.7241704303212', '1125.1238146762557'),
					 (['tai6', ' kɔk7'], '1129.4362068765622', '1129.782129747608'),
					 (['siu1', ' ki5'], '1139.4718929883484', '1140.0388011745194'),
					 (['si2', ' si2'], '1143.9308421977134', '1144.479158180978'),
					 (['pueʔ9', ' to6'], '1148.0978914030584', '1148.6096204642909'),
					 (['ʔioʔ0', ' ke5'], '1152.2783176253208', '1152.7931613143085'),
					 (['po3', ' pue5'], '1156.3852844729308', '1156.9508753147318'),
					 (['sit7', ' tiək7'], '1161.04846997452', '1161.456628384793'),
					 (['kuaʔ9', ' pau1'], '1173.4419008996606', '1173.9456464707907'),
					 (['tsioʔ0', ' te6'], '1178.01779967664', '1178.5158458816973'),
					 (['tsu3', ' sik8'], '1182.4801487453972', '1182.8590465394532'),
					 (['pak7', ' kik8'], '1193.5919853693606', '1193.9356191780976'),
					 (['pueʔ9', ' paʔ7'], '1198.7652808421597', '1199.146376853966'),
					 (['si2', ' ke5'], '1203.8546320704768', '1204.4339930017738'),
					 (['paʔ9', ' ʔioʔ8'], '1209.0170149228052', '1209.38470200435'),
					 (['kɔ1', ' tok8'], '1213.5276033368666', '1213.9179948539115'),
					 (['tik7', ' ko1'], '1235.8878616416903', '1236.3855784163734'),
					 (['si5', ' pau1'], '1244.7255961772587', '1245.3664759613578'),
					 (['kau3', ' paʔ7'], '1249.4467841869205', '1249.8692240180396'),
					 (['peʔ0', ' pit7'], '1253.6425090718087', '1254.0064087499554'),
					 (['tsap8', ' si5'], '1257.7514684600917', '1258.2160387054143'),
					 (['ka1', ' to1'], '1262.1236660193654', '1262.6101373666377'),
					 (['tɤ3', ' ki1'], '1266.9737667576849', '1267.4964089916625'),
					 (['tua6', ' ki2'], '1271.4346219071642', '1271.9571454639229'),
					 (['tsui3', ' ko3'], '1282.8908968243584', '1283.3738257927077'),
					 (['tiʔ9', ' tsui3'], '1291.9006671756667', '1292.3897937006677'),
					 (['to3', ' kɔk7'], '1307.5471004986275', '1307.9222988420559'),
					 (['te6', ' ki1'], '1312.16053031611', '1312.6387320092138'),
					 (['tɤ3', ' ki2'], '1316.7793695146777', '1317.2782750976028'),
					 (['pai2', ' kai3'], '1334.810537189457', '1335.2934914566094'),
					 (['si5', ' kak7'], '1349.6648332013813', '1350.1230750505167'),
					 (['kɔ3', ' tɔ1'], '1365.2727207916191', '1365.7773800634122'),
					 (['te2', ' kɔ3'], '1375.2054184636415', '1375.7693746736545'),
					 (['toʔ9', ' pɔ5'], '1380.076663535092', '1380.5411237886885'),
					 (['pat8', ' toʔ7'], '1384.8828516934332', '1385.2733384698709'),
					 (['tsui3', ' tiʔ7'], '1389.133038456038', '1389.5760168819531'),
					 (['kɔk7', ' sut8'], '1393.564649075771', '1393.94105307327'),
					 (['ki2', ' tsioʔ8'], '1404.4330229829445', '1404.878948141667'),
					 (['tu1', ' pai2'], '1412.9994503507382', '1413.4875350661173'),
					 (['kɔk7', ' ki2'], '1417.9373823762742', '1418.4078352251474'),
					 (['kek7', ' ko3'], '1422.2285414399355', '1422.7461758435838'),
					 (['kɔ3', ' tsa3'], '1432.633872581168', '1433.1732948803592'),
					 (['ka1', ' kau5'], '1445.6656159008055', '1446.1782443023797'),
					 (['sik8', ' te2'], '1451.0183660018274', '1451.6043470430982'),
					 (['ko1', ' kui5'], '1457.1980034204573', '1457.638719152405'),
					 (['tua6', ' tsui3'], '1461.7075602856196', '1462.2462300467719'),
					 (['po4', ' tui6'], '1466.1362311155037', '1466.6240710803736'),
					 (['kɔk7', ' ka1'], '1470.3250321653968', '1470.7700832245332'),
					 (['be4', ' ti1'], '1474.615003519159', '1475.221244908366'),
					 (['bi4', ' hun3'], '1484.5714041808308', '1485.2105335597298'),
					 (['bi4', ' tsʰi4'], '1489.3111315673664', '1489.9896475510668'),
					 (['tiʔ9', ' huiʔ7'], '1493.9447818972856', '1494.4743338899762'),
					 (['po6', ' tui6'], '1504.933429306757', '1505.442235224202'),
					 (['ki5', ' tsia3'], '1509.565634048103', '1510.0923436437142'),
					 (['peʔ0', ' ko3'], '1529.3357807900811', '1529.8635894177553'),
					 (['si5', ' ti6'], '1541.100093493598', '1541.6698848899055'),
					 (['kau3', ' tsioʔ8'], '1545.5069343739158', '1546.0228333313567')]
		答案 = ([['Di002', '魚骨', 'hɯ2 kut7', ''], ['Di008', '隔腹', 'keʔ paʔ', ''], ['Di010', '市價', 'tshi4 ke5', ''], ['Di011', '對質', 'tui tsiʔ', ''], 
			['Di018', '道家', 'to4 ka1', ''], ['Di026', '買菜', 'be4 tshaj5', ''], ['Di034', '保護', 'po3 hɔ6', ''], ['Di036', '肥豬', 'pui2 tɨ1', ''], ['Di038', '吃多', 'tsiaʔ0 tsue6', ''], 
			['Di040', '設計', 'siæt7 ke5', ''], ['Di043', '駕駛', 'ka5 sɯ3', ''], ['Di044', '割貨', 'kuaʔ9 hɤ5', ''], ['Di051', '豬肚', 'tɨ1 tɔ6', ''], ['Di055', '靜靜', 'tsiəŋ4 tsiəŋ4', ''],
			 ['Di060', '九石', 'kau tsioʔ', ''], ['Di064', '國事', 'kɔk7 sɯ6', ''], ['Di067', '百期', 'paʔ ki', ''], ['Di070', '規矩', 'kui1 kɨ3', ''], ['Di090', '割塊', 'kuaʔ9 hɤ5', ''], 
			 ['Di100', '百劇', 'paʔ kiok78', ''], ['Di102', '學習', 'hak8 sip8', ''], ['Di108', '魚價', 'hɯ2 ke5', ''], ['Di115', '這次', 'tsit pai', ''], ['Di117', '買卡', 'be4 kha3', ''], 
			 ['Di119', '交保', 'kau po', ''], ['Di125', '市面', 'tshi4 bin6', ''], ['Di129', '白色', 'peʔ0 siək7', ''], ['Di130', '學士', 'hak8 sɨ6', ''], ['Di131', '過度', 'kɤ5 tɔ6', ''], 
			 ['Di140', '八道', 'pue? to7?6', ''], ['Di142', '甲組', 'kaʔ9 tsɔ1', ''], ['Di147', '北埔', 'pak7 pɔ1', ''], ['Di150', '肥魚', 'pui2 hɨ2', ''], 
			 ['Di151', '足好', 'tsiok7 ho3', ''], ['Di154', '慈悲', 'tsu2 pi1', ''], ['Di155', '教師', 'kau5 sɯ1', ''], ['Di160', '布袋', 'pɔ5 tɤ6', ''], 
			 ['Di161', '報價', 'po5 ke5', ''], ['Di162', '白豬', 'peʔ0 tɨ1', ''], ['Di164', '悲劇', 'pi1 kiok8', ''], ['Di168', '過期', 'kɤ5 ki2', ''], ['Di171', '收據', 'siu1 kɨ5', ''], 
			 ['Di173', '八道', 'pueʔ to', ''], ['Di179', '煮熟', 'tsɨ3 siək8', ''], ['Di186', '寄藥', 'kia5 ʔioʔ8', ''], ['Di188', '九百', 'kau paʔ', ''], ['Di196', '買角', 'be4 kak7', ''], 
			 ['Di201', '知己', 'ti1 ki3', ''], ['Di204', '巴結', 'pa1 ket7', ''], ['Di211', '豬排', 'tɨ1 pai2', ''], ['Di214', '過失', 'kɤ5 sit7', ''], ['Di217', '熟茶', 'siək8 te2', ''], ['Di224', '米市', 'bi4 tshi4', ''], ['Di229', '四弟', 'sɨ5 ti6', '']], [(['hu2', ' kut7'], '18.77385414161029', '19.26625697137455'), (['keʔ7', ' paʔ7'], '64.3107333966327', '64.65126500530717'), (['tsʰi4', ' ke5'], '73.38725533052218', '73.97269770352064'), (['tui3', ' tsiʔ7'], '86.75663471321866', '87.1205208425927'), (['to4', ' kɛ1'], '142.2470076170122', '142.71355864779437'), (['be4', ' tsʰi5'], '188.9110828308377', '189.44525845626603'), (['huat7', ' kut8'], '233.76359947753613', '234.25650032442988'), (['po3', ' hu6'], '244.9596979177678', '245.43301865727216'), (['pui2', ' tu1'], '260.4503542149177', '260.88912151481605'), (['tsiaʔ0', ' tse6'], '270.4529640420197', '271.0504964102799'), (['sia7', ' ke5'], '288.00558294830546', '288.65504822028004'), (['ka5', ' sai3'], '337.7598312408766', '338.33862008449756'), (['kuaʔ9', ' hue5'], '347.48640098869345', '348.0566193281041'), (['tu1', ' tɔ6'], '393.17327268544545', '393.66799552332617'), (['kau3', ' tsioʔ0'], '484.39660952422565', '484.91410370018207'), (['kɔk7', ' su6'], '502.75866057023285', '503.2476910535085'), (['paʔ9', ' ki2'], '519.3673721929092', '519.8991056897158'), (['kuaʔ9', ' te5'], '639.548054310972', '640.0429483452327'), (['paʔ7', ' kiok8'], '695.4778510110069', '695.8523392249789'), (['hap8', ' sip8'], '705.156620937327', '705.6121397686705'), (['hu2', ' ke5'], '733.9648892628604', '734.4883020158439'), (['tsit7', ' pai3'], '783.8109660495544', '784.2698262053647'), (['ka1', ' po3'], '805.4725935784446', '805.9785725172052'), (['tsʰi4', ' bin6'], '840.5554065626824', '841.0795900064151'), (['peʔ0', ' sik7'], '860.5813579683232', '860.9403573519172'), (['hak8', ' si6'], '865.7406734036113', '866.2688110031347'), (['kue5', ' tɔ6'], '872.1191717921001', '872.644187209126'), (['pueʔ7', ' to6'], '943.2837326365517', '943.7793163570075'), (['pui2', ' hu2'], '1007.3343019844381', '1007.8308244362789'), (['tsok7', ' ho3'], '1013.2531724192727', '1013.7727319842563'), (['kau5', ' su1'], '1045.8308642826296', '1046.3724560671317'), (['pɔ5', ' te6'], '1069.9634008501828', '1070.4849242090215'), (['po5', ' kɛ5'], '1074.3260050706838', '1074.8276552233865'), (['peʔ0', ' tu1'], '1079.0699317456622', '1079.5631256116185'), (['kue5', ' ki2'], '1120.5801918487223', '1121.0683213210946'), (['siu1', ' ki5'], '1139.4718929883484', '1140.0388011745194'), (['pueʔ9', ' to6'], '1148.0978914030584', '1148.6096204642909'), (['tsu3', ' sik8'], '1182.4801487453972', '1182.8590465394532'), (['kau3', ' paʔ7'], '1249.4467841869205', '1249.8692240180396'), (['tu1', ' pai2'], '1412.9994503507382', '1413.4875350661173'), (['sik8', ' te2'], '1451.0183660018274', '1451.6043470430982'), (['bi4', ' tsʰi4'], '1489.3111315673664', '1489.9896475510668'), (['si5', ' ti6'], '1541.100093493598', '1541.6698848899055')], [['隔壁', 'keʔ9 piaʔ7'], ['不時', 'put7 si2'], ['姑嫂', 'kɔ1 so3'], ['貼布', 'taʔ9 pɔ5'], ['地圖', 'te6 tɔ2'], ['高級', 'ko1 kip7'], ['八支', 'pueʔ9 ki1'], ['排隊', 'pai2 tui6'], ['步數', 'pɔ6 sɔ5'], ['著急', 'tioʔ0 kip7'], ['道德', 'to6 tik7'], ['補習', 'pɔ3 sip8'], ['石佛', 'tsioʔ0 hut8'], ['報國', 'po5 kɔk7'], ['白白', 'peʔ0 peʔ8'], ['道教', 'to6 kau5'], ['滴雨', 'tiʔ9 hɔ6'], ['姑婆', 'kɔ1 po2'], ['道家', 'to6 ka1'], ['對句', 'tui5 ku5'], ['對敵', 'tui5 tik8'], ['八排', 'pueʔ9 pai2'], ['報時', 'pɔ5 si2'], ['第十', 'te6 tsap8'], ['時局', 'si2 kiɔk8'], ['發掘', 'huat7 sut8'], ['買毒', 'be4 tok8'], ['第四', 'te6 si5'], ['買紙', 'be4 tsua3'], ['白豆', 'peʔ0 tau6'], ['舅公', 'ku4 koŋ1'], ['滑倒', 'kut8 to3'], ['時機', 'si2 ki1'], ['百九', 'paʔ9 kau3'], ['習題', 'sit8 tue2'], ['倒台', 'to3 tai2'], ['五十', 'go4 tsap8'], ['失陪', 'sit7 pue2'], ['效果', 'hau6 ko3'], ['棋道', 'ki2 to6'], ['吃素', 'tsiaʔ0 sɔ5'], ['寶地', 'po3 te6'], ['茶杯', 'te2 pue1'], ['地球', 'te6 kiu2'], ['瀉藥', 'siaʔ9 ʔioʔ8'], ['石猴', 'tsioʔ0 kau2'], ['大舌', 'tua6 tsiʔ8'], ['美麗', 'bi4 le6'], ['石葉', 'tsioʔ0 hioʔ8'], ['佛教', 'hut8 kau5'], ['拜佛', 'pai5 put8'], ['法術', 'huat7 sut8'], ['白布', 'peʔ0 pɔ5'], ['百倍', 'paʔ9 pɤ6'], ['不過', 'put7 ko5'], ['咬刀', 'ka6 to1'], ['石鼓', 'tsioʔ0 kɔ3'], ['白刀', 'peʔ0 to1'], ['學者', 'hak8 tsia3'], ['告辭', 'ko5 si2'], ['北部', 'pak7 pɔ6'], ['學校', 'hak8 hau6'], ['豬舌', 'tɨ1 tsiʔ8'], ['報紙', 'po5 tsua3'], ['石膏', 'tsioʔ0 ko1'], ['收筆', 'siu1 pit7'], ['道教', 'to4 kau5'], ['吃茶', 'tsiaʔ0 te2'], ['保庇', 'po3 pi5'], ['毒菇', 'tɔk8 kɔ1'], ['以前', 'ʔi4 tsiəŋ2'], ['十支', 'tsap8 ki1'], ['格局', 'keʔ9 kiɔk8'], ['奇怪', 'ki2 kuai5'], ['球桌', 'kiu2 toʔ7'], ['八嫂', 'pueʔ9 so3'], ['買魚', 'be4 hi2'], ['石虎', 'tsioʔ0 hɔ3'], ['特別', 'tik8 piӕt8'], ['十九', 'tsap8 kau3'], ['標記', 'piau1 ki6'], ['八期', 'pueʔ9 ki2'], ['白旗', 'peʔ0 ki2'], ['指數', 'tsi3 sɔ5'], ['國寶', 'kɔk7 po3'], ['買旗', 'be4 ki2'], ['基地', 'ki1 te6'], ['道德', 'to4 tik7'], ['大刀', 'tua6 to1'], ['地步', 'te6 pɔ6'], ['買竹', 'be4 tik7'], ['五毒', 'go4 tok8'], ['實在', 'sit8 tsai6'], ['雞婆', 'kue1 po2'], ['孤枝', 'kɔ1 ki1'], ['學期', 'hak8 ki2'], ['水色', 'tsui3 sik7'], ['寶島', 'po3 to3'], ['卜卦', 'pok7 kua5'], ['寶刀', 'po3 to1'], ['好茶', 'ho3 te2'], ['徒弟', 'tɔ2 tue6'], ['服藥', 'hok8 ʔioʔ8'], ['失敗', 'sit7 pai6'], ['買米', 'be4 bi4'], ['雨滴', 'hɔ6 tiʔ7'], ['德國', 'tik7 kɔk7'], ['背熟', 'pue6 sik8'], ['敵機', 'tik8 ki1'], ['表弟', 'piau3 te6'], ['排骨', 'pai2 kut7'], ['厚厚', 'kau6 kau6'], ['藥水', 'ʔioʔ0 tsui3'], ['排水', 'pai2 tsui3'], ['敵國', 'tik8 kɔk7'], ['竹北', 'tik7 pak7'], ['旗號', 'ki2 ho6'], ['毒計', 'tok8 ke5'], ['一滴', 'tsit8 tiʔ7'], ['解決', 'kai3 kuat8'], ['拜四', 'pai5 si5'], ['合時', 'hap8 si2'], ['八號', 'pueʔ9 ho6'], ['包輸', 'pau1 su1'], ['魚池', 'hɯ2 ti2'], ['故交', 'kɔ5 kau1'], ['第九', 'te6 kau3'], ['其實', 'ki2 sit8'], ['大國', 'tai6 kɔk7'], ['時時', 'si2 si2'], ['藥價', 'ʔioʔ0 ke5'], ['寶貝', 'po3 pue5'], ['失德', 'sit7 tiək7'], ['割包', 'kuaʔ9 pau1'], ['石地', 'tsioʔ0 te6'], ['北極', 'pak7 kik8'], ['八百', 'pueʔ9 paʔ7'], ['時價', 'si2 ke5'], ['百藥', 'paʔ9 ʔioʔ8'], ['孤獨', 'kɔ1 tok8'], ['竹篙', 'tik7 ko1'], ['四包', 'si5 pau1'], ['白筆', 'peʔ0 pit7'], ['十四', 'tsap8 si5'], ['剪刀', 'ka1 to1'], ['短枝', 'tɤ3 ki1'], ['大旗', 'tua6 ki2'], ['水果', 'tsui3 ko3'], ['滴水', 'tiʔ9 tsui3'], ['島國', 'to3 kɔk7'], ['地基', 'te6 ki1'], ['短期', 'tɤ3 ki2'], ['排解', 'pai2 kai3'], ['四角', 'si5 kak7'], ['古都', 'kɔ3 tɔ1'], ['茶古', 'te2 kɔ3'], ['桌布', 'toʔ9 pɔ5'], ['別桌', 'pat8 toʔ7'], ['水滴', 'tsui3 tiʔ7'], ['國術', 'kɔk7 sut8'], ['奇石', 'ki2 tsioʔ8'], ['國旗', 'kɔk7 ki2'], ['結果', 'kek7 ko3'], ['古早', 'kɔ3 tsa3'], ['家教', 'ka1 kau5'], ['高貴', 'ko1 kui5'], ['大水', 'tua6 tsui3'], ['部隊', 'po4 tui6'], ['國家', 'kɔk7 ka1'], ['買豬', 'be4 ti1'], ['米粉', 'bi4 hun3'], ['滴血', 'tiʔ9 huiʔ7'], ['部隊', 'po6 tui6'], ['記者', 'ki5 tsia3'], ['白果', 'peʔ0 ko3'], ['九石', 'kau3 tsioʔ8']])
		結果 = 音標比對excel(檔案, 問題)
		self.assertEqual(答案, 結果)
	
if __name__ == '__main__':
	unittest.main()
