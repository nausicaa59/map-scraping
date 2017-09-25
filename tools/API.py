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
	except Exception as e:
		print("erreur : reponse invalide, détail : ", e)


def postNbConnectes(nb, url):
	pass


def getAuteurRandom():
	r = requests.get(config.API_PATH_AUTEUR_RANDOM)
	return r.json()


def getAuteurRandomByLetter(letters):
	r = requests.get(config.API_PATH_AUTEUR_UNTREATED_BY_LETTER + letters)
	return r.json()


def postUpdateAuteur(auteur):
	try:
		start = time.time()
		r = requests.post(config.API_PATH_AUTEUR_UPDATE, json = {"auteur": auteur})
		rjson = r.json()
		end = time.time()
		print(auteur["pseudo"],"Traité en :", str(end - start), "s")
		if rjson["formatErreur"] != [] or rjson["fatalError"]:
			print("Erreur formatage :", rjson["formatErreur"])
			print("Detail :", rjson["formatValide"])
			print("fatalError :", rjson["fatalError"])
			print(auteur)
	except Exception as e:
		print("erreur : reponse invalide, détail : ", e)	