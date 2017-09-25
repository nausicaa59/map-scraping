from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import profils.profil as profil
import tools.generateurUrl as generateurUrl
import tools.API as API
import config
import time
import sys
import random
import requests


def getOptionConsol(defaultOption):
	for arg in sys.argv:
		if arg.find("-letter=") is not -1:
			defaultOption["letters"] = arg.replace("-letter=","")

	return defaultOption



def run(options):
	headers = {'User-Agent': 'Chrome/39.0.2171.95'}
	pseudos = API.getAuteurRandomByLetter(options["letters"])

	for pseudo in pseudos:
		try:
			pathProfil = config.PATERN_PATH_AUTEUR_PROFIL.replace("[X]", pseudo.lower())
			response = requests.get(pathProfil, headers=headers)
			infos = profil.infos(response.content)
			infos["pseudo"] = pseudo
			API.postUpdateAuteur(infos)
			del response

		except requests.exceptions.RequestException as e:
			print(pseudo, "erreur du traitement :", e)
			time.sleep(20)



options = {"letters" : False}
options = getOptionConsol(options)

if options["letters"] == False:
	print("aucune lettres choisi, fin du procéssus")

run(options)

