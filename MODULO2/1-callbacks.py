import requests
import threading

def get_pokemon(response):
    results = response.json().get('forms')
    name = results[0].get('name')
    print(f'pokemon: {name}')
    
def error():
    print('no es posible ejecutar la función')
    
def get_request(url,success_callback,error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response)
    else:
        error_callback()
        
if __name__ == '__main__':
    for i in range(1,20):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        thread = threading.Thread(target=get_request,
                                  kwargs={'url':url,
                                          'success_callback':get_pokemon,
                                          'error_callback':error
                                        })
        thread.start()