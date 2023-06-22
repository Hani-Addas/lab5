'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    # Test out the get_pokemon_info() function
    random_pokemon = get_pokemon_info()

    # Use breakpoints to view returned dictionary
    poke_info = get_pokemon_info("Rockruff")
    for p in poke_info['results']:
        print(p['pokemon infor:'])
    return

def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # TODO: Clean the Pokemon name parameter
    clean_name = str(pokemon_name).strip().lower()

    # TODO: Build a clean URL and use it to send a GET request
    print(f'Getting information for {pokemon_name}...', end='')
    url = POKE_API_URL + clean_name
    resp_msg =requests.get(url)
    # TODO: If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp_msg.status_code == requests.code.ok:
        print('success')
        return resp_msg.text 

    # TODO: If the GET request failed, print the error reason and return None
    else:
        print('failure')
        print(f'Response code:{resp_msg.status_code} ({resp_msg.reason})')

    return

if __name__ == '__main__':
    main()