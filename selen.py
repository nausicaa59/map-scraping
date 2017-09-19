from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import profils.pageliste as profilPageliste
import tools.generateurUrl as generateurUrl
import tools.API as API
import config
import time
import sys
import random


def extractsCurrent(driver):
	sujets = profilPageliste.sujets(driver.page_source)
	nbConnectes = profilPageliste.nbConnectes(driver.page_source) 
	API.postListSujet(sujets)
	API.postNbConnectes(nbConnectes, driver.current_url)	


def callNextButton(driver):
	driver.find_element_by_css_selector(".pagi-precedent-actif").click()
	extractsCurrent(driver)



def run(startUrl):
	driver = webdriver.Chrome(config.PATH_DRIVER_GOOGLE)
	driver.get(startUrl)
	extractsCurrent(driver)
	maxError = 10
	currentError = 0

	while True:
		try:
			time.sleep(2)
			callNextButton(driver)
			currentError = 0
			print("-- En attente --")			
		except Exception as e:
			print("erreur lors de la selection du bt suivant :", e)
			currentError += 1
			if currentError > maxError:
				sys.exit(0)
		


def getOptionConsol(defaultOption):
	for arg in sys.argv:
		if arg.find("-random=") is not -1:
			defaultOption["random"] = True
			defaultOption["maxRandom"] = int(arg.replace("-random=",""))
			defaultOption["startUrl"] = generateurUrl.homePageRandom(0, defaultOption["maxRandom"])
		if arg.find("-id=") is not -1:
			idA = arg.replace("-id=","")
			defaultOption["startUrl"] = generateurUrl.homePage(idA)

	return defaultOption	




options = {
	"random" : False,
	"maxRandom" : 20000,
	"startUrl" : config.PATH_INIT_PAGE_LISTE		
}

options = getOptionConsol(options)
run(options["startUrl"])
