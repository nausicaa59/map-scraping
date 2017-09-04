import config
import random

def homePageRandom(minV = 0, maxV = 10):
	if minV >= maxV:
		minV = 0
		maxV = 10
	
	page = random.randint(minV, maxV)
	nbTopic = (25*page) + 1
	urlPage = config.PATERN_PATH_PAGE_LISTE.replace("[X]", str(nbTopic))
	return urlPage


def userProfil(pseudo):
	return config.PATERN_PATH_AUTEUR_PROFIL.replace("[X]", pseudo)