import requests

base_URL = 'https://pokeapi.co/api/v2/'
def get_info(name):
    url = f'{base_URL}/pokemon/ditto{name}'
    response = requests.get(url)
    print(response)

poki_name = 'Pikachu'
get_info(poki_name)