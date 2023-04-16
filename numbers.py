from paho.mqtt.client import Client

from time import sleep
from random import random,randint
import sys

# Función para determinar si un número es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Función para procesar los mensajes recibidos
def on_message(mqttc, userdata, message):
    numero = float(message.payload)
    try:
        num = float(numero)
        if num.is_integer():
            # Si el número es entero
            print(f"Entero recibido: {int(num)}") 
            userdata['Frec_enteros'] += 1           
            mqttc.publish('numbers/frec_entero', str(userdata['Frec_enteros']))
            mqttc.publish('numbers/entero', str(int(num)))
            # Comprobamos si el número recibido es primo
            if es_primo(int(num)):
                print(f"El número {int(num)} es primo")
                mqttc.publish('numbers/entero/primo', str(int(num)))
            else:
                print(f"El número {int(num)} no es primo")
                mqttc.publish('numbers/entero/no_primo', str(int(num)))
        else:
            # Si el número es real
            print(f"Real recibido: {num}")
            userdata['Frec_reales'] += 1
            mqttc.publish('numbers/frec_real', str(userdata['Frec_reales']))
            mqttc.publish('numbers/real', str(num))
   
    except ValueError:
        print(f"Mensaje inválido recibido: {payload}")




def main(hostname):

    userdata = {'Frec_enteros' : 0, 'Frec_reales' : 0}
    mqttc = Client(userdata = userdata)
    
    mqttc.on_message = on_message
    print(f'connecting {hostname}...', end='\n')
    mqttc.connect(hostname)
    print('OK.')
    
    mqttc.subscribe('numbers')
 
    print('publishing')

    mqttc.loop_forever()
    

if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)
