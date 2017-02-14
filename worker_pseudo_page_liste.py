import tools
import pymysql
import time
import sys
import extraction.pageliste
import extraction.topic
import models.auteur as auteur
import models.message as message


#----------------------------------
#recherche argument...
#----------------------------------
maxRandom = 20000
modeEtendu = 0

for arg in sys.argv:
	if arg.find("-max=") is not -1:
		maxRandom = int(arg.replace("-max=",""))
	if arg.find("-etendu=") is not -1:
		modeEtendu = int(arg.replace("-etendu=",""))

print("Options choisi : max="+str(maxRandom) + " - modeEtendu=" + str(modeEtendu))


#Ouverture connexion
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='packing', autocommit=True)
cur = conn.cursor()


while True:
	url = auteur.genererUrlHomePageRandom(0,maxRandom)
	htmlPageList = tools.simpleGetRequest(url)

	listAuteurs = extraction.pageliste.users(htmlPageList)
	sousLiens = extraction.pageliste.liens(htmlPageList)
	
	print("[URL-LISTE] ("+url+") En cours de traitement...")
	auteur.adds(listAuteurs, cur)

	#on parcours chaque sousliensliens...
	if modeEtendu > 0:
		for souslien in sousLiens:
			topicLien = souslien
			print("[URL-TOPIC] En cours de traitement...")
			
			while True:
				html = tools.simpleGetRequest(topicLien)				
				listAuteurs = extraction.topic.users(html)
				topicLien = extraction.topic.pagesuivante(html)	
				auteur.adds(listAuteurs, cur)				
				#messages = extraction.topic.messages(html)
				#message.addMultiples(messages, souslien, cur)
								
				if topicLien is None:
					break
				else:
					topicLien = "http://www.jeuxvideo.com/" + topicLien
					time.sleep(5)

			time.sleep(5)	

	print("---------------------------")
	print("Attente avant reprise...")
	print("---------------------------")
	time.sleep(5)


#Fermeture connexion
conn.close()