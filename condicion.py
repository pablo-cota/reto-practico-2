import threading
from time import sleep
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

# método que requiere la condición
def comprar_pan(condicion):
    with condicion:
        logging.debug('Esperando por el pan')
        condicion.wait()
        print(threading.current_thread().name + ' compró el pan') 

# método que prepara el pan
def preparar_pan(condicion):
    logging.debug('Preparando pan')
    sleep(1)
    logging.debug('Pan listo')
    sleep(0.001)
    with condicion:
        condicion.notify_all()

# creación de condición
condicion = threading.Condition()

# crear hilos
threading.Thread(target=comprar_pan, args=(condicion,),name="hilo comprador 1").start()
threading.Thread(target=comprar_pan, args=(condicion,),name="hilo comprador 2").start()
threading.Thread(target=comprar_pan, args=(condicion,),name="hilo comprador 3").start()

sleep(1) # esperar un segundo para demostrar que los hilos compradores esperan por el pan

# se crea el hilo que prepara el pan
threading.Thread(target=preparar_pan, args=(condicion,),name="hilo panadero").start()

# join 
for i in threading.enumerate():
    if i.name.startswith("hilo"):
        i.join()