import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
		for p in scdb:
			p['Score'] = int (p['Score'])
			p['Age'] = int (p['Age'])
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
	while(True):
		inputstr = (input("Score DB > ")) 
		if inputstr == "": continue
		parse = inputstr.split(" ")
		if parse[0] == 'add':
			try:
				record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
				scdb += [record]
			except: continue
			#add 잘못입력시 프로그램 꺼지는거 수정 
		elif parse[0] == 'inc':
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						num = int(p['Score'])
						num += int(parse[2])
						p['Score'] = str(num)
						print(p)
			except: continue
			#inc 잘못 입력시 프로그램 꺼지는거 수정
		#inc 생성 
		elif parse[0] == 'find':
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						print(p)
			except: continue
			#find	 잘못 입력시 프로그램 꺼지는거 수정
		#find 생성
		elif parse[0] == 'del':
			try:
				for p in scdb:
					if p['Name'] == parse[1]:
						scdb.remove(p)
						if p['Name'] == parse[1]:
							scdb.remove(p)
			except: continue
			#del 잘못 입력시 프로그램 꺼지는거 수정
		#del 오류 수정 	
		elif parse[0] == 'show':
			try:
				sortKey ='Name' if len(parse) == 1 else parse[1]
				showScoreDB(scdb, sortKey)
			except: continue
			#show 뒤에 무언가 입력시 프로그램 종료되던거 수정
		elif parse[0] == 'quit':
			break
		else:
			print("Invalid command: " + parse[0])

	
def showScoreDB(scdb, keyname):
	for p in sorted(scdb, key=lambda person: person[keyname]):
		for attr in sorted(p):
			print(attr + "=" + p[attr], end=' ')
		print()
	


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
 
