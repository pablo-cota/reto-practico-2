import threading


# recurso compartido por todos los hilos
contador = 0

# función que se ejecutará como hilo

def cuenta(limite, bloqueo):
    global contador
    
    for _ in range(limite):
        # bloquear acceso a recurso compartido
     ##   bloqueo.acquire()
        contador += 1
        # liberar acceso a recurso compartido
      ##  bloqueo.release()


# objeto para realizar un bloqueo
lock = threading.Lock()

# creación de los hilos
hilo1 = threading.Thread(target=cuenta, name='Hilo-1',
                         args=(50000, lock))
hilo2 = threading.Thread(target=cuenta, name='Hilo-2',
                         args=(50000, lock))

# iniciar el funcionamiento de los hilos
hilo1.start()
hilo2.start()

# esperar por la terminación de ambos hilos
hilo1.join()
hilo2.join()

print(f'Contador: {contador}')