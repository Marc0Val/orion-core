import RPi.GPIO as GPIO
from src.utils.mqtt_client import OrionMQTT

class OrionRelays:
    def __init__(self):
        # Configuración de Pines extraída de su configuración 
        self.MAIN_LIGHT = 17 
        self.AMBIENT_LIGHT = 16
        
        # Lógica de Relevador: Activo Bajo 
        self.ON = GPIO.LOW
        self.OFF = GPIO.HIGH
        
        self.mqtt = OrionMQTT()
        self.setup_gpio()

    def setup_gpio(self):
        """Inicialización de los pines físicos en el NSR """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.MAIN_LIGHT, GPIO.OUT, initial=self.OFF)
        GPIO.setup(self.AMBIENT_LIGHT, GPIO.OUT, initial=self.OFF)

    def toggle_light(self, pin, state):
        """Cambia el estado de un relé específico"""
        target_state = self.ON if state == "ON" else self.OFF
        GPIO.output(pin, target_state)
        return "Encendido" if target_state == self.ON else "Apagado"

    def on_message(self, client, userdata, msg):
        """Escucha comandos desde la red MQTT"""
        payload = msg.payload.decode().upper()
        
        if msg.topic == "orion/nsr/lights/main":
            status = self.toggle_light(self.MAIN_LIGHT, payload)
            print(f"Luz Principal: {status}")
            
        elif msg.topic == "orion/nsr/lights/ambient":
            status = self.toggle_light(self.AMBIENT_LIGHT, payload)
            print(f"Luz Ambiental: {status}")

    def run(self):
        self.mqtt.connect()
        # Suscripción a los tópicos de control 
        self.mqtt.subscribe("orion/nsr/lights/main", self.on_message)
        self.mqtt.subscribe("orion/nsr/lights/ambient", self.on_message)
        print("Músculo (Relés): ONLINE y esperando impulsos.")

if __name__ == "__main__":
    relays = OrionRelays()
    relays.run()