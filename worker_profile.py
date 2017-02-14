import tools
import pymysql
import time
import extraction.profil
import models.auteur as m_auteur
import notification.worker.profile as notif


#Ouverture connexion
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='packing', autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)


while True:
	#on tire un utilisateur au hasard...
	auteurTirage = m_auteur.getRandomNonTraite_Profil(cur)
	if auteurTirage == False:
		time.sleep(3)
		continue


	#on recherche le profil html
	html = tools.simpleGetRequest("http://www.jeuxvideo.com/profil/#?mode=infos".replace("#", auteurTirage["pseudo"]))
	if html == False:
		notif.ko()
		time.sleep(3)
		continue


	#on tente une extraction d'info
	info = extraction.profil.infos(html)
	notif.en_cours(auteurTirage, info)
	if m_auteur.isAnomalieInfo(info) == True:
		m_auteur.updateChekedProfil(cur, auteurTirage["id"], 2)
		notif.ko_info_invalide()
		time.sleep(3)
		continue


	#on update le profil + on marque l'utilisateur comme fait...
	try:
		m_auteur.updateProfil(cur, info, auteurTirage["id"])
		m_auteur.updateChekedProfil(cur, auteurTirage["id"], 1)
		notif.ok()
	except pymysql.err.ProgrammingError as e:
		m_auteur.updateChekedProfil(cur, auteurTirage["id"], 2)
		notif.ko_exception(e)


	notif.attente()
	time.sleep(3)


#Fermeture connexion
conn.close()
