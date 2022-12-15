import threading
from time import sleep
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

# método que activa el evento
def make_ping(event):
    logging.debug('PING!!!')
    event.set()

# método que requiere un evento para continuar
def make_pong(event):
    # esperar por el evento
    logging.debug('//Esperando por PING')
    event.wait()
    logging.debug('PONG!!!')


# creación de evento
event = threading.Event()

# crear hilos

# se crea el hilo que requiere el evento
threading.Thread(target=make_pong, args=(event,),name="hilo pong").start()

sleep(1) # esperar un segundo para demostrar que el hilo pong espera por el evento

# se crea el hilo que activa el evento
threading.Thread(target=make_ping, args=(event,),name="hilo ping").start()