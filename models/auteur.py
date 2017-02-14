import tools
import extractiondata
import random

urlIndexForum = "http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm"
urlPaternIndexForum = "http://www.jeuxvideo.com/forums/0-51-0-1-0-[index]-0-blabla-18-25-ans.htm"
urlPaternAuteurAbonnes = "http://www.jeuxvideo.com/profil/[X]?mode=abonne"
urlPaternRechercheAuteurTopic = "http://www.jeuxvideo.com/recherche/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm?search_in_forum=[X]&type_search_in_forum=auteur_topic"
urlPaternRechercheAuteurMessage = "http://www.jeuxvideo.com/recherche/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm?search_in_forum=[X]&type_search_in_forum=texte_message"


def genererUrlHomePageRandom(minV = 0, maxV = 10):
	if minV >= maxV:
		minV = 0
		maxV = 10
	
	page = random.randint(minV, maxV)
	nbTopic = (25*page) + 1
	urlPage = urlPaternIndexForum.replace("[index]", str(nbTopic))
	return urlPage


def jamaisTraite(bdd, auteur):
	return getByPseudo(bdd, auteur) == []


#-------------------------
# BDD opération
#-------------------------
def add(bdd, val):
	sql = "INSERT INTO `auteurs` (`id`, `pseudo`, `created_at`, `updated_at`) VALUES (NULL, '"+ val["pseudo"] +"', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
	bdd.execute(sql)
	return bdd.lastrowid


def all(bdd):
	sql = "SELECT * FROM `auteurs`;"
	bdd.execute(sql)
	return list(bdd)


def get(bdd, id):
	sql = "SELECT * FROM `auteurs` WHERE id ='"+ str(id) +"';"
	bdd.execute(sql)
	return list(bdd)


def getByPseudo(bdd, pseudo):
	sql = "SELECT * FROM `auteurs` WHERE pseudo ='"+ pseudo +"';"
	bdd.execute(sql)
	return list(bdd)		


def getRandomNonTraite_Profil(bdd):
	sql = "SELECT * FROM `auteurs` WHERE cheked_profil = '0' ORDER BY RAND() LIMIT 1";
	bdd.execute(sql)
	resultat = bdd.fetchall()

	if len(resultat) > 0:
		return resultat[0]
	else:
		return False


def updateProfil(bdd, info, idPseudo):
	f_sql = ''
	first = True
	for cle, value in info.items():
		if value != False:
			f_sql += "" if first else ","
			f_sql += " "+cle+"='"+str(value)+"'"
			first = False

	if f_sql != '':
		sql = "UPDATE auteurs SET " + f_sql + " where id = '" + str(idPseudo) +"'"
		bdd.execute(sql)


def isAnomalieInfo(info):
	for cle, value in info.items():
		if value != False:
			return False
	return True


def updateChekedProfil(bdd, idPseudo, status):
	sql = "UPDATE auteurs SET cheked_profil = '" + str(status) +"' where id ='" + str(idPseudo) + "'"
	bdd.execute(sql)


def debugFile(html, name):
	with open("debug/"+name, 'w') as out_file:
		out_file.write(html)


def adds(listAuteurs, cur):
	compteurInconnu = 0
	compteurConnu = 0

	for cible in listAuteurs:
		cible = cible.lower()
		if jamaisTraite(cur, cible):
			compteurInconnu += 1
			add(cur, {"pseudo": cible})	
		else:
			compteurConnu += 1

	print(str(compteurInconnu)+" personne ajouter "+str(compteurConnu)+" personne connus")


def proximite(pseudo, limite, bdd):
	sql = "SELECT * FROM auteurs ORDER BY jaro_winkler_similarity(%s, pseudo) DESC LIMIT 0,%s";
	bdd.execute(sql,(pseudo,limite))
	resultat = bdd.fetchall()
	return resultat