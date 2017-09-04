from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import profils.pageliste as profilPageliste
import tools.generateurUrl as generateurUrl
import tools.API as API
import config
import time
import sys


def extractsCurrent(driver):
	sujets = profilPageliste.sujets(driver.page_source)
	nbConnectes = profilPageliste.nbConnectes(driver.page_source) 
	API.postListSujet(sujets)
	API.postNbConnectes(nbConnectes, driver.current_url)	


def callNextButton(driver):
	driver.find_element_by_css_selector(".pagi-suivant-actif").click()
	extractsCurrent(driver)
	print("-- En attente --")
	time.sleep(10)


def run(startUrl):
	driver = webdriver.Chrome(config.PATH_DRIVER_GOOGLE)
	driver.get(startUrl)
	extractsCurrent(driver)

	while True:
		callNextButton(driver)


def getOptionConsol(defaultOption):
	for arg in sys.argv:
		if arg.find("-random=") is not -1:
			defaultOption["random"] = True
			defaultOption["maxRandom"] = int(arg.replace("-random=",""))

	if defaultOption["random"]:
		defaultOption["startUrl"] = generateurUrl.homePageRandom(0, defaultOption["maxRandom"])

	return defaultOption	




options = {
	"random" : False,
	"maxRandom" : 20000,
	"startUrl" : config.PATH_INIT_PAGE_LISTE		
}

options = getOptionConsol(options)
run(options["startUrl"])
