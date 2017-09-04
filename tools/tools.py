import re
import config


def regexOnlyValue(patern, candidat):
	resultat = re.findall(patern, candidat)
	if len(resultat) > 0 :
		return resultat[0]
	else :
		return False


def decryptageUrl(candidat):
	base16 = "0A12B34C56D78E9F";
	str_ = ""
	rurl = "" 
	ch = 0
	cl = 0
	j = 0
	
	fragments = candidat.split(" ")
	for fragment in fragments:
		if len(fragment) > len(str_):
			str_ = fragment
	

	for i in range(0,len(str_)-1,2):
		ch = base16.find(str_[i])
		cl = base16.find(str_[i+1])
		rurl += chr((ch*16) + cl)

	print(rurl)


def creer_fichier_proximite(nom, extension, contenu, racine = ""):
	dossier1 = False
	dossier2 = False
	dossier3 = False
	path = racine + ""

	if len(nom) == 0:
		return False

	if len(nom) == 1:
		dossier1 = nom[0]

	if len(nom) == 2:
		dossier1 = nom[0]
		dossier2 = nom[1]

	if len(nom) > 2:
		dossier1 = nom[0]
		dossier2 = nom[1]
		dossier3 = nom[2]
	
	if dossier1 != False:
		path += dossier1 + "/"
		if os.path.isdir(path) != True:
			os.mkdir(path)

	if dossier2 != False:
		path += dossier2 + "/"
		if os.path.isdir(path) != True:
			os.mkdir(path)

	if dossier3 != False:
		path += dossier3 + "/"
		if os.path.isdir(path) != True:
			os.mkdir(path)

	path += nom + extension

	with open(path, "w") as ficher:
		ficher.write(contenu)
