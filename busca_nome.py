import requests

def surch_random_name():
    data = requests.get("https://randomuser.me/api") # faz a requisicao da api
    data = data.json()
    nome = data['results'][0]['name']['first'] # busca o pirmeiro nome do arq json
    print(nome) # printa ele no terminal

surch_random_name()