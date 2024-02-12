import threading
import time

from concurrent.futures import Future

def callback_future(future):
    print('hola, esto se ejecuta cuando el llegue al futuro')
    print(f' el futuro es {future.result()}')
    
if __name__ == '__main__':
    future = Future()
    future.add_done_callback(callback_future)
    
    print('Iniciando ...')
    
    time.sleep(2)
    print('Terminado...')
    print('llegamos al futuro')
    future.set_result('Edteam')
    
    print('el futuro es ahora!!!')