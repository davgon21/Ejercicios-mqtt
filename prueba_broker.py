from paho.mqtt.client import Client


def on_message(mqttc, userdata, msg):  
    print("MESSAGE:", userdata, msg.topic, msg.qos, msg.payload, msg.retain)


def on_publish(mqttc, userdata, mid):
    print("Mensaje con el topic clients publicado")
    
        
def main(broker, topic):
    mqttc = Client()
 
    mqttc.on_message = on_message
    print(f'connecting {broker}...', end='\n')
    mqttc.connect(broker)
    print('OK.')
    
    mqttc.subscribe(topic)
    mqttc.on_publish = on_publish
    
    mqttc.loop_start()

    while True:
       # se espera a que el usuario escriba un mensaje
       mensaje = input("Ingrese el mensaje a enviar: ")
      
       # se publica el mensaje en el tema "prueba"
       mqttc.publish(topic , mensaje)

	# se detiene el bucle de mensajes
    mqttc.loop_stop()
     # mqttc.loop_forever() # No es necesario pues equivale a usar mqttc.loop_start() y      mqttc.loop_stop()
    
    
if __name__ == "__main__":
    import sys
    if len(sys.argv)<3:
        print(f"Usage: {sys.argv[0]} broker topic")
        sys.exit(1)
    broker = sys.argv[1]
    topic  = sys.argv[2]
    main(broker, topic)





