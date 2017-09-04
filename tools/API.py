import config
import json
import requests


def postListSujet(sujets):
	r = requests.post(config.API_PATH_POST_LIST_SUJET, json = {"sujets": sujets})
	print(r.json())


def postNbConnectes(nb, url):
	print(json.dumps({"nb": nb, "urlCurrent": url}))