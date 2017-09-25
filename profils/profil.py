import re
import tools
import config
import datetime
from bs4 import BeautifulSoup



def getLigneInfo(infoGenerales):
	lignes = []

	if len(infoGenerales) == 0:
		return lignes

	for ligne in infoGenerales[0].select("li"):
		lib = None
		value = None
		selectLib = ligne.select(".info-lib")
		selectValue = ligne.select(".info-value")

		if selectLib != []:
			lib = selectLib[0].get_text().strip().lower()

		if selectValue != []:
			value = selectValue[0].get_text().strip().lower()

		if lib != None and value != None:
			lignes.append((lib, value))

	return lignes



def findLigneByLabel(lignes, label):
	for ligne in lignes:
		if ligne[0].find(label) != -1:
			return ligne[1]

	return None



def getNbMessage(lignes):
	value = findLigneByLabel(lignes, "messages")
	if value == None:
		return 0

	value = value.replace(".", "")
	recherche = re.findall("([0-9]*)", value)
	return int(recherche[0]) if len(recherche) > 0 else 0



def getDateInscription(lignes):
	value = findLigneByLabel(lignes, "depuis")
	if value == None:
		return "1980-01-01 00:00:00"

	recherche = re.findall("([0-9]*) jours", value.replace(".", ""))
	if len(recherche) > 0:
		if recherche[0].isdigit() is True:
			date = datetime.date.today() - datetime.timedelta(days = int(recherche[0]))
			return date.strftime('%Y-%m-%d %H:%M:%S')
	
	return "1980-01-01 00:00:00"



def getAvatar(s):
	selectAvatar = s.select("#header-profil .content-img-avatar img");
	if selectAvatar == []:
		return config.PATH_DEFAULT_AVATAR

	return selectAvatar[0]["src"]



def getNbAbonne(s):
	value = None
	selectMenu = s.select(".list-menu-profil")

	if len(selectMenu) == 0:
		return 0
	
	for span in selectMenu[0].select("span"):
		if span.get_text().find("Abonn") != -1:
			value = span.get_text()
	
	if value == None:
		return 0

	recherche = re.findall("\(([0-9]*)\)", value.replace(".", ""))
	if len(recherche) > 0 :
		return int(recherche[0])

	return 0



def isBanned(s):
	alerts = s.select(".alert-row")
	for alert in alerts:
		txt = alert.get_text()
		if txt.find("banni") != -1:
			return 1

	imagesErreurs = s.select(".img-erreur")
	if len(imagesErreurs) > 0:
		return 1
	
	return 0
	


def infos(html):
	soup = BeautifulSoup(html, 'html.parser')
	infoGenerales = soup.select(".bloc-default-profil .display-line-lib");
	lignes = getLigneInfo(infoGenerales)

	return {
		"date_inscription" : getDateInscription(lignes),
		"nb_messages": getNbMessage(lignes),
		"img_lien" : getAvatar(soup),		
		"nb_relation" : getNbAbonne(soup),
		"banni" : isBanned(soup)		
	}
