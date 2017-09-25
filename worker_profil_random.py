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


def run():
	while True:
		try:
			start = time.time()
			auteur = API.getAuteurRandom()
			end = time.time()
			if len(auteur) == 0:
				time.sleep(3)
				continue

			pathProfil = config.PATERN_PATH_AUTEUR_PROFIL.replace("[X]", auteur[0]["pseudo"].lower())
			headers = {'User-Agent': 'Chrome/39.0.2171.95'}
			response = requests.get(pathProfil, headers=headers)
			
			infos = profil.infos(response.content)
			infos["pseudo"] = auteur[0]["pseudo"]
			
			API.postUpdateAuteur(infos)
			del response

		except requests.exceptions.RequestException as e:
			print("Erreur lors de l'ouverture de "+lien)
			return False

		#time.sleep(1)



run()

