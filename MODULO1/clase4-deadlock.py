import threading
import time

recurso_1 = threading.Lock()
recurso_2 = threading.Lock()

def proceso_1():
    with recurso_1:
        print('Proceso 1 tiene recurso 1')
        time.sleep(1)
        print('Proceso 1 esperando por recurso 2')
        with recurso_2:
            print('Proceso 1 tiene recurso 2')
            
def proceso_2():
    with recurso_1:
        print('Proceso 2 tiene recurso 2')
        time.sleep(1)
        print('Proceso 2 esperando por recurso 1')
        with recurso_2:
            print('Proceso 2 tiene recurso 1')
            
thread_1 = threading.Thread(target=proceso_1)
thread_2 = threading.Thread(target=proceso_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()