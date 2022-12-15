import threading
import time


# función que se ejecutará como hilo
def tarea():
    nombre = threading.current_thread().getName()
    print(f'{nombre} - esperando')
    orden = barrera.wait()      # barrera de parada para el hilo
    time.sleep(orden)
    print(f'{nombre} - ({orden}) - barrera pasada')


# creación de la barrera
barrera = threading.Barrier(3) 

# creación de los hilos
hilo1 = threading.Thread(target=tarea, name='Hilo-1')
hilo2 = threading.Thread(target=tarea, name='Hilo-2')

# iniciar del funcionamiento de los hilos
hilo1.start()
time.sleep(1)
hilo2.start()

# liberar la barrera de ambos hilos
orden = barrera.wait()
time.sleep(3)
print(f'Hilo principal - ({orden}) - barrera pasada')

hilo1.join()
hilo2.join()

print('Fin hilo principal')