def add(val, url, bdd):
	if getByDataId(bdd, val["dataId"]) == []:
		tuple_data = (val["pseudo"],url,val["message"],val["titre"],val["dataId"])
		bdd.execute("INSERT INTO `messages` (`pseudo`, `url`, `message`, `titre`, `dataId`) VALUES (%s,%s,%s,%s,%s);", tuple_data)
		return bdd.lastrowid
	return False


def addMultiples(messages, url, bdd):
	compteurNew = 0
	compteurOld = 0
	
	for message in messages:
		if add(message, url, bdd) is False:
			compteurOld += 1
		else:
			compteurNew += 1

	#print(str(compteurNew) + " nouveau message, " + str(compteurOld) + " non ajoutés")


def getByDataId(bdd, dataId):
	sql = "SELECT * FROM `messages` WHERE dataId = %s;"
	bdd.execute(sql, (dataId))
	return list(bdd)