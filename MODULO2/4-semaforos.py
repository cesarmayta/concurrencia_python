import threading

semaforo1 = threading.Semaphore(0)
semaforo2 = threading.Semaphore(0)

def fun_1():
    print(1)
    semaforo1.release()
    semaforo2.acquire()
    print(3)
    semaforo1.release()
    
def fun_2():
    semaforo1.acquire()
    print(2)
    semaforo2.release()
    semaforo1.acquire()
    print(4)
    
threading.Thread(target=fun_1).start()
threading.Thread(target=fun_2).start()

