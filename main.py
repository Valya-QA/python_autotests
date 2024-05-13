import requests
URL = 'https://api.pokemonbattle.me/v2'
TOKEN = ''
HEADER ={'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Масик",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    
    "pokemon_id": "26669",
    "name": "BOBO",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_pokeball = {
    "pokemon_id":"26669"
}

response_create = requests.post (url = f'{URL}/pokemons', headers=HEADER, json=body_create)
print (response_create.text)
message = response_create.json()['message']
print(message)
response_change = requests.put (url = f'{URL}/pokemons', headers=HEADER, json=body_change)
print (response_change.text)
message = response_change.json()['message']
print(message)
response_pokeball = requests.post (url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print (response_pokeball.text)
message = response_pokeball.json()['message']
print(message)

