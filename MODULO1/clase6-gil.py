import time
import threading

def contador(number):
    while number > 0:
        number -=1

if __name__ == '__main__':
    start = time.time()

    count = 1000000000

    #contador(count)
    t1 = threading.Thread(target=contador,args=(count/3,))
    t2 = threading.Thread(target=contador,args=(count/3,))
    t3 = threading.Thread(target=contador,args=(count/3,))
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()

    print(f'Tiempo transcurrido {time.time() - start }')