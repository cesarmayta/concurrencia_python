import time
import queue
import threading

def mostrar_cola():
    while not queue.empty():
        item = queue.get()
        print(f'valor : {item}')
        queue.task_done()
        time.sleep(1)
        
if __name__ == '__main__':
    queue = queue.Queue() #FIFO FISRT IN FIRST OUT
    
    for val in range(1,20):
        queue.put(val)
        
    print('la cola esta llena')
    
    for _ in range(4):
        thread = threading.Thread(target=mostrar_cola)
        thread.start()