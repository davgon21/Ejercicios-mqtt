from paho.mqtt.client import Client
import traceback
import sys

#Tomamos el sensor 2 y elegimos como valores de temperatura y humedad
temp = 15 
hum = 35 #si la temperatura baja de temp o el valor de humidity sube de hum entonces
#el cliente dejará de escuchar en el topic humidity

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)
    n = float (msg.payload)
    if msg.topic == 'temperature/temp2':
        if n > temp and userdata['humidity'] == 'No Suscrito': #el valor de temperatura es superior a t de luego el cliente se suscribe al topic humidity
            mqttc.subscribe('humidity')
            userdata['humidity'] = 'Suscrito' #suscrito a humidity
        elif n < temp and userdata['humidity'] == 'Suscrito': #el valor de temperatura es inferior a t de luego el cliente se suscribe al topic humidity
            mqttc.unsubscribe('humidity') #deja de estar suscrito a humidity
            userdata['humidity'] = 'No suscrito'
    elif msg.topic == 'humidity':
        if n > hum: #el valor de humidity sube de K1 entonces el cliente se desuscribe del topic humidity
            mqttc.unsubscribe('humidity')
            userdata['humidity'] = 'No suscrito'
            
def main(hostname):
    userdata = {
        'humidity':'No Suscrito'
    }
    mqttc = Client(userdata= userdata)
    mqttc.on_message = on_message
    
    print(f'connecting {hostname}...', end='\n')
    mqttc.connect(hostname)
    print('OK.')

    mqttc.subscribe('temperature/temp2')

    mqttc.loop_forever()

if __name__ == "__main__":
    if len(sys.argv)<2:
        print(f"Usage: {sys.argv[0]} broker")
    broker = sys.argv[1]
    main(broker)
