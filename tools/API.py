import config
import json
import requests
import time

def postListSujet(sujets):
	try:
		start = time.time()
		r = requests.post(config.API_PATH_POST_LIST_SUJET, json = {"sujets": sujets})
		rjson = r.json()
		end = time.time()
		print("-------------------------------")
		print("Traité en :", str(end - start), "s")
		print("Erreur critique :", rjson["fatalError"])
		print("Nombre d'erreur :", rjson["nbErreur"])
		print("Nombre d'item (json) valide :", rjson["nbValide"])
		print("Nombre de sujet ajouté :", rjson["nbAjouter"])
		print("Nombre de sujet rejeter insertion :", rjson["nbNonAjouter"])
		#print("détaille rejet :")
		#for rejet in rjson["notificationError"]:
		#	print(rejet)
	except Exception as e:
		print("erreur : reponse invalide, détail : ", e)


def postNbConnectes(nb, url):
	pass
	#print(json.dumps({"nb": nb, "urlCurrent": url}))