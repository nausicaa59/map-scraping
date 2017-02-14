"""
Fonctions d'extractions d'information appartir de contenu html
sur le model de Jquery pour les pages listes
"""


from pyquery import PyQuery as pq
import tools
import datetime


def users(html):
	reponse = []
	d = pq(html)
	elementAuteurs = d(".topic-list .topic-author");
	
	for elementAuteur in elementAuteurs:
		pseudo = d(elementAuteur).text()
		pseudo = pseudo.replace("\\n", "")
		pseudo = pseudo.replace(" ", "")
		if pseudo != "Auteur":
			reponse.append(pseudo)

	return reponse


def liens(html):
	reponse = []
	d = pq(html)
	liens = d(".lien-jv.topic-title")

	for itemLien in liens:
		if d(itemLien).parents(".topic-delete").length == 0:
			url = "http://www.jeuxvideo.com/" + d(itemLien).attr("href")
			reponse.append(url)

	return reponse


def nb_connection(html):
	d = pq(html)
	nb = d(".nb-connect-fofo").html();
	nb = tools.regexOnlyValue("([0-9]*)",nb)