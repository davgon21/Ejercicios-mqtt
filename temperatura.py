from paho.mqtt.client import Client
from time import sleep
import sys

# Configuración del broker MQTT y los subtopics de temperatura
TEMPERATURE_1 = []
TEMPERATURE_2 = []
TEMPERATURE_3 = []

TEMPERATURE_TOPIC = "temperature/"
T1 = "temperature/temp1"
T2 = "temperature/temp2"
T3 = "temperature/temp3"

# Función para calcular la temperatura máxima, mínima y media
def max_min_avg():
    max_temp1 = max(TEMPERATURE_1)
    min_temp1 = min(TEMPERATURE_1)
    avg_temp1 = sum(TEMPERATURE_1) / len(TEMPERATURE_1)
    
    max_temp2 = max(TEMPERATURE_2)
    min_temp2 = min(TEMPERATURE_2)
    avg_temp2 = sum(TEMPERATURE_2) / len(TEMPERATURE_2)
    
    max_temp3 = max(TEMPERATURE_3)
    min_temp3 = min(TEMPERATURE_3)
    avg_temp3 = sum(TEMPERATURE_3) / len(TEMPERATURE_3)
    
    print(f'SENSOR 1 - Max: {max_temp1}, Min: {min_temp1}, Media: {avg_temp1}')
    print(f'SENSOR 2 - Max: {max_temp2}, Min: {min_temp2}, Media: {avg_temp2}')
    print(f'SENSOR 3 - Max: {max_temp3}, Min: {min_temp3}, Media: {avg_temp3}')
    

# Función para procesar los mensajes MQTT de temperatura
def on_message(mqttc, userdata, message):
    # Obtener el nombre del sensor
    sensor_name = message.topic
    
    # Convertir el valor del mensaje a temperatura (asumiendo que es un número)
    temperature = float(message.payload.decode())
    
    # Almacenar el valor de temperatura para el sensor correspondiente
    if sensor_name == T1:
        TEMPERATURE1.append(temperature)
    elif sensor_name == T2:
        TEMPERATURE2.append(temperature)
    else :
    	TEMPERATURE3.append(temperature)
    	

    
def main(hostname):
    mqttc = Client()
    
    print(f'connecting {hostname}...', end='\n')
    mqttc.connect(hostname)
    print('OK.')
    
    mqttc.on_message = on_message
    
    mqttc.subscribe('temperature/#')
    mqttc.loop_start()

    while True:
        sleep(3) 
        max_min_avg()
        
    client.loop_stop()

if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)

