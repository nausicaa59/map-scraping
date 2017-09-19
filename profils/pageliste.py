"""
Fonctions d'extractions d'information appartir de contenu html
sur le model de Jquery pour les pages listes
"""


from pyquery import PyQuery as pq
import tools.tools as tools
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


def sujets(html):
	reponse = []
	d = pq(html)
	liens = d(".lien-jv.topic-title")

	for itemLien in liens:
		reponse.append({
			'url' : "http://www.jeuxvideo.com" + d(itemLien).attr("href"),
			'date': d(itemLien).parent().parent().find(".topic-date .lien-jv").text(),
			'nbReponse' : int(d(itemLien).parent().parent().find(".topic-count").text()),
			'auteur': cleanPseudo(d(itemLien).parent().parent().find(".topic-author").text())
		})

	return reponse


def nbConnectes(html):
	d = pq(html)
	nb = d(".nb-connect-fofo").html();
	nb = tools.regexOnlyValue("([0-9]*)",nb)
	return nb


def cleanPseudo(pseudo):
	pseudo = pseudo.replace("\\n", "")
	pseudo = pseudo.replace(" ", "")
	return pseudo