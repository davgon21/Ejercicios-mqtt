from paho.mqtt.client import Client
import time, sys
from time import sleep

# función que se ejecuta cuando se recibe un mensaje
def on_message(mqttc, userdata, message):
    payload = message.payload.decode('utf-8')
    tiempo_esp = userdata['tiempo'] 
    print(f"Se ha publicado el mensaje con {tiempo_esp} segundos de espera")
    
    



def main(broker):
    userdata = {'tiempo' : 0}
    mqttc = Client(userdata = userdata)
    mqttc.on_message = on_message
    
    print(f'connecting {broker}...', end='\n')
    mqttc.connect(broker)
    print('OK.')
    
    mqttc.loop_start()
    
    while True:
        topic = input('Dame un topic:')
        mqttc.subscribe(topic)
        tiempo_espera = input('Dame un tiempo de espera:')
        mensaje  = input('¿Qué mensaje quieres que publique?')
        userdata['tiempo'] = int(tiempo_espera)
        sleep(int(tiempo_espera))
        mqttc.publish(topic, mensaje)
        
    mqttc.loop_stop()
    

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: {} broker".format(sys.argv[0]))
        sys.exit(1)
    broker = sys.argv[1]
    main(broker)




