"""
Fonctions d'extractions d'information appartir de contenu html
sur le model de Jquery
"""


from pyquery import PyQuery as pq
import tools
import datetime


def messages(html):
	reponse = []
	d = pq(html)
	d = d.remove('blockquote')
	d = d.remove('.signature-msg')
	d = d.remove('.text-enrichi-forum a')
	titre = d("#bloc-title-forum").text()
	nodesMessages = d(".bloc-message-forum")	

	for node in nodesMessages:
		auteur = d(node).find(".bloc-pseudo-msg.text-user").text()
		auteur = auteur.replace("\\n", "")
		auteur = auteur.replace(" ", "")
		message = d(node).find(".bloc-contenu").text()
		dataId = d(node).attr("data-id")
		
		reponse.append({
			"pseudo":auteur,
			"message":message,
			"titre":titre,
			"dataId":dataId
		})

	return reponse


def users(html):
	reponse = []
	d = pq(html)
	elementAuteurs = d(".bloc-pseudo-msg")
	
	for elementAuteur in elementAuteurs:
		pseudo = d(elementAuteur).text()
		pseudo = pseudo.replace("\\n", "")
		pseudo = pseudo.replace(" ", "")
		if pseudo != "Auteur":
			reponse.append(pseudo)

	return reponse


def pagesuivante(html):
	reponse = []
	d = pq(html)
	NextPage = d(".page-active ~ span a").attr("href");
	return NextPage