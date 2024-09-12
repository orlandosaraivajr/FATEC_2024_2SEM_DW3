import requests
URL = 'https://pokeapi.co/api/v2/pokemon/1'
req = requests.get(URL)
dados_recebidos = req.json()
print(dados_recebidos.get('moves')[0].get('move').get('name'))