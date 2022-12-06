import requests
import json

token = '4fd1cebc3092f4c8a7280c28ac9c2144'
response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Fly",
    "photo": "https://fs-prod-cdn.nintendo-europe.com/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_pokemonlegendsarceus/CI_NSwitch_PokemonLegendsArceus_Rowlet_Official_image950w.png"
})

print(response.text)

response_put = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1409,
    "name": "FlyFly",
    "photo": ""
})

print(response.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": 1409,
})

print(response.text)
