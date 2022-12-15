import threading
import time


# función que se ejecutará como hilo
def tarea(semaforo):
    nombre = threading.current_thread().name
    time.sleep(0.2)
    print(f'{nombre} - esperando')
    # esperar por el semáforo
    with semaforo:
        print(f'{nombre} - trabajando')
        time.sleep(1)


# objeto semáforo limitado a dos
semaphore = threading.Semaphore(2)
    
# creación de los hilos
hilo1 = threading.Thread(target=tarea, name='Hilo-1',
                         args=(semaphore,))
hilo2 = threading.Thread(target=tarea, name='Hilo-2',
                         args=(semaphore,))
hilo3 = threading.Thread(target=tarea, name='Hilo-3',
                         args=(semaphore,))
hilo4 = threading.Thread(target=tarea, name='Hilo-4',
                         args=(semaphore,))

# iniciar el funcionamiento de los hilos
hilo1.start()
time.sleep(0.2)
hilo2.start()
time.sleep(0.2)
hilo3.start()
time.sleep(0.2)
hilo4.start()

# esperar por la terminación de los hilos
hilo1.join()
hilo2.join()
hilo3.join()
hilo4.join()

print('Fin hilo principal')