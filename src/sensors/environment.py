import Adafruit_DHT
import time
import json
from src.utils.mqtt_client import OrionMQTT

class EnvironmentSensor:
    def __init__(self):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = 4  # Pin BCM extraído de su configuración previa
        self.mqtt = OrionMQTT()
        self.mqtt.connect()
        self.topic = "orion/nsr/sensors/dht11"

    def read_data(self):
        """Lee humedad y temperatura del sensor físico"""
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        
        if humidity is not None and temperature is not None:
            return {
                "temperature": round(temperature, 1),
                "humidity": round(humidity, 1),
                "status": "ONLINE"
            }
        else:
            return {"status": "ERROR", "message": "Fallo en lectura de sensor"}

    def run(self):
        print("Sentidos climáticos: ACTIVADOS")
        while True:
            data = self.read_data()
            # Publicamos el JSON con la telemetría ambiental
            self.mqtt.publish(self.topic, json.dumps(data))
            
            # Un pequeño log interno para depuración en el NSR
            if data["status"] == "ONLINE":
                print(f"Telemetría: {data['temperature']}°C | {data['humidity']}%")
            
            time.sleep(30) # Lectura cada 30 segundos para evitar estrés en el sensor

if __name__ == "__main__":
    env = EnvironmentSensor:
    env.run()