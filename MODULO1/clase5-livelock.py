import threading
import time

recurso_1 = threading.Lock()
recurso_2 = threading.Lock()

def proceso(numero,lock1,lock2):
    while True:
        with lock1:
            print(f'Proceso {numero} tiene recurso 1')
            time.sleep(0.1)
            print(f'Proceso {numero} esperando por recurso 2')
            with lock2:
                print(f'Proceso {numero} tiene recurso 2')
            
            
thread_1 = threading.Thread(target=proceso,args=(1,recurso_1,recurso_2))
thread_2 = threading.Thread(target=proceso,args=(2,recurso_2,recurso_1))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()