"""
Fonctions d'extractions d'information appartir de contenu html
sur le model de Jquery
"""


from pyquery import PyQuery as pq
import tools
import datetime


def infos(html):
	d = pq(html)
	info = {
		"pays" : False,
		"nb_messages": False,
		"img_lien" : False,		
		"nb_relation" : False,
		"banni" : False,
		"date_inscription" : False
	}


	nbEnfant = d(".display-line-lib li").length
	for i in range(nbEnfant):
		candidat = d(".display-line-lib .info-lib").eq(i);
		candidat = candidat.html()

		if candidat is not None:
			candidat = candidat.replace("\\n","")
			candidat = candidat.replace("\\t","")
			candidat = candidat.replace(" ","")
		
		if candidat == "Membredepuis:" :
			date_inscription_s = d(".display-line-lib .info-value").eq(i);
			if date_inscription_s.html() != None:
				date_inscription_b = date_inscription_s.html()
				date_inscription_b = date_inscription_b.replace(".", "")
				date_inscription_b = tools.regexOnlyValue("([0-9]*) jours", date_inscription_b)
				if date_inscription_b is not False:
					if date_inscription_b.isdigit() is True:
						info["date_inscription"] = datetime.date.today() - datetime.timedelta(int(date_inscription_b))
		
		if candidat == "MessagesForums:" :
			nb_messages_s = d(".display-line-lib .info-value").eq(i);
			if nb_messages_s.html() != None:
				nb_messages_b = nb_messages_s.html()
				nb_messages_b = nb_messages_b.replace(".", "")
				nb_messages_b = tools.regexOnlyValue("([0-9]*)", nb_messages_b)	
				if nb_messages_b != "" and nb_messages_b is not False:
					info["nb_messages"] = nb_messages_b

		if candidat == "Pays:" :
			pays_s = d(".display-line-lib .info-value").eq(i);
			if pays_s.html() != None:
				pays_b = pays_s.html()
				pays_b = pays_b.replace("\n", "")
				pays_b = pays_b.replace("\\n", "")
				pays_b = pays_b.replace(" ", "")
				info["pays"] = pays_b


	img_lien_s = d(".content-img-avatar img");
	if img_lien_s.attr("src") != None:
		img_lien_b = img_lien_s.attr("src")
		info["img_lien"] = img_lien_b

	nb_relation_s = d("ul.list-menu-profil li:last-child span.JvCare");
	if nb_relation_s.html() != None:
		nb_relation_b = nb_relation_s.html()
		nb_relation_b = nb_relation_b.replace(".", "")
		nb_relation_b = tools.regexOnlyValue("\(([0-9]*)\)", nb_relation_b)	
		info["nb_relation"] = nb_relation_b

	banni_s = d(".alert-danger");
	if banni_s.html() != None:
		info["banni"] = "1"

	return info
