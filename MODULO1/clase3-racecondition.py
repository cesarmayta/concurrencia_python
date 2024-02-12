import threading

contador = 0

lock = threading.Lock()

def sumar_contador():
    global contador
    for _ in range(1000000):
        with lock:
            contador += 1
        
def restar_contador():
    global contador
    for _ in range(1000000):
        with lock:
            contador -= 1
        
thread1 = threading.Thread(target=sumar_contador)
thread2 = threading.Thread(target=restar_contador)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('valor final del contador : ',contador)