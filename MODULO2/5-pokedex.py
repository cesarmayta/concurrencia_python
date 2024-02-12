import threading
import queue
import requests
import time

pokedapi_url = 'https://pokeapi.co/api/v2/pokemon/'

def fetch_pokemon(pokemon_name,cola):
    try:
        response = requests.get(pokedapi_url + pokemon_name)
        data = response.json()
        cola.put(data)
    except Excpetion as e:
        print(f'error {e}')
        
def main():
    lista_pokemons = ['bulbasaur','charmander','squirtle','pikachu','snorlax']
    
    cola = queue.Queue()
    
    threads = []
    for name in lista_pokemons:
        thread = threading.Thread(target=fetch_pokemon,args=(name,cola))
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    while not cola.empty():
        result = cola.get()
        print(f"Nombre pokemon : {result['name']}")
        print(f"id : {result['id']}")
        print("="*20)
        
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f' tiempo : {end - start} segundos')