import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

# Cargamos nuestra identidad secreta
load_dotenv(dotenv_path="config/.env")

class OrionMQTT:
    """El sistema nervioso de O.R.I.O.N. [cite: 196]"""
    
    def __init__(self):
        self.host = os.getenv("MQTT_HOST", "localhost")
        self.port = int(os.getenv("MQTT_PORT", 1883))
        self.user = os.getenv("MQTT_USER")
        self.password = os.getenv("MQTT_PASS")
        self.client = mqtt.Client()

        if self.user and self.password:
            self.client.username_pw_set(self.user, self.password)

    def connect(self):
        try:
            self.client.connect(self.host, self.port, 60)
            self.client.loop_start()
            return True
        except Exception as e:
            print(f"Error de conexión neural: {e}")
            return False

    def publish(self, topic, message):
        """Envía un impulso eléctrico (mensaje) a la constelación [cite: 196]"""
        self.client.publish(topic, str(message))

    def subscribe(self, topic, callback):
        """Escucha un canal específico de la red [cite: 196]"""
        self.client.subscribe(topic)
        self.client.on_message = callback

if __name__ == "__main__":
    # Prueba rápida de conectividad
    test_node = OrionMQTT()
    if test_node.connect():
        print("Sistema Nervioso: ONLINE")
        test_node.publish("orion/test", "O.R.I.O.N. despierta...")