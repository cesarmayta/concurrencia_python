import requests
import threading

def get_pokemon(pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    if response.status_code == 200:
        results = response.json().get('forms')
        name = results[0].get('name')
        
        print(f'{pokemon_id} : {name}')
        
if __name__ == '__main__':
    for i in range(1,150):
        thread = threading.Thread(target=get_pokemon,args=[i])
        thread.start()
        #get_pokemon(i)