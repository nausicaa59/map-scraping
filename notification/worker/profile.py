def en_cours(auteurTirage, info):
	print("["+auteurTirage["pseudo"]+", id="+str(auteurTirage["id"])+"] en cours de traitement")
	print("Valeur trouvée :"+str(info))	


def ok():
	print("[OK]La mise a jours a été effecutée")


def ko():
	print("Erreur, opération annulée")


def ko_exception(e):
	print("[KO] La requete d'update a échouée... " + str(e))


def ko_info_invalide():
	print("[KO] Le profils ne présente aucune valeurs valide...")


def attente():
	print("---------------------------")
	print("Attente avant reprise...")
	print("---------------------------")
