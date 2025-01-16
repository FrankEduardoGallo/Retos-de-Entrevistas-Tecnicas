import paho.mqtt.client as mqtt

# Variables de configuración
BROKER_URL = "paranoid.lat"
PORT = 8083
TOPIC = "prueba/sensor/temperatura"

# Función de conexión
def on_connect(client, userdata, flags, rc):
    print('Conectado con el código de estado: %d' % rc)
    print('Conexión exitosa. Suscribiéndome al tópico "%s"' % TOPIC)
    client.subscribe(TOPIC, qos=2)  # Suscripción al tópico

# Función para manejar los mensajes
def on_message(client, userdata, message):
    print('------------------------------')
    print('Tópico: %s' % message.topic)
    print('Contenido del mensaje: %s' % message.payload.decode())
    print('QoS: %d' % message.qos)

# Función principal que ejecuta el cliente MQTT
def main():
    # Crear cliente MQTT con ID único y sesión persistente
    client = mqtt.Client(client_id='albert-subs', clean_session=False)
    
    # Registrar las funciones de callback
    client.on_connect = on_connect
    client.on_message = on_message
    
    # Conectar al broker MQTT
    client.connect(host=BROKER_URL, port=PORT)
    
    # Iniciar el loop de eventos de MQTT
    client.loop_forever()

if __name__ == '__main__':
    main()
