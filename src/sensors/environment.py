import adafruit_dht
import board
import time
import json
from src.utils.mqtt_client import OrionMQTT

class EnvironmentSensor:
    def __init__(self):
        # Usamos board.D4 para el Pin 4 BCM [cite: 186]
        self.device = adafruit_dht.DHT11(board.D4)
        self.mqtt = OrionMQTT()
        self.mqtt.connect()
        self.topic = "orion/nsr/sensors/dht11"

    def read_data(self):
        try:
            temperature = self.device.temperature
            humidity = self.device.humidity
            if temperature is not None and humidity is not None:
                return {
                    "temperature": round(temperature, 1),
                    "humidity": round(humidity, 1),
                    "status": "ONLINE"
                }
        except RuntimeError as e:
            # Los DHT11 suelen fallar lecturas ocasionalmente, es normal
            return {"status": "READ_ERROR", "message": str(e)}
        except Exception as e:
            return {"status": "CRITICAL_ERROR", "message": str(e)}
        return {"status": "WAITING"}

    def run(self):
        print("Sentidos climáticos (CircuitPython): ACTIVADOS")
        while True:
            data = self.read_data()
            if data["status"] == "ONLINE":
                self.mqtt.publish(self.topic, json.dumps(data))
                print(f"Telemetría: {data['temperature']}°C | {data['humidity']}%")
            time.sleep(30)