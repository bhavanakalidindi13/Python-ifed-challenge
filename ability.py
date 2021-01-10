import requests


def ability(pokemon_name):
    pokemon_details = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    abilities = []
    for pokemon_ability in pokemon_details['abilities']:
        abilities.append(pokemon_ability['ability']['name'])
    return abilities
