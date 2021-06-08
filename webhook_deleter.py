import requests

webhook = input("Entrez le lien du webhook a supprimer: ")

try:
    requests.delete(webhook)
    print("WebHook supprimé !")
except:
    print("Erreur dans la suppresion !")