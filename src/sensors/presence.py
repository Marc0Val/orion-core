import os
import subprocess
import time
from src.utils.mqtt_client import OrionMQTT

class PresenceSensor:
    def __init__(self):
        # Identificadores extraídos de su 'vieja configuración'
        self.devices = {
            "PHONE_WIFI": "3a:30:57:0d:6a:ec",
            "PHONE_BT": "6C:F7:84:60:D3:3A",
            "PC_NET": "00:45:e2:c1:b0:d1",
            "WATCH_BT": "F4:B4:F7:23:1C:EA"
        }
        self.mqtt = OrionMQTT()
        self.mqtt.connect()

    def scan_wifi(self, mac):
        """Escaneo ARP para detectar dispositivos en la red local"""
        try:
            # Buscamos en la tabla ARP del NSR (Pi 4B)
            output = subprocess.check_output(["arp", "-a"]).decode("utf-8")
            return mac.lower() in output.lower()
        except Exception:
            return False

    def scan_bluetooth(self, mac):
        """Escaneo de proximidad BT (Requiere bluez instalado en el host)"""
        try:
            # Comando ligero para verificar presencia sin emparejar
            result = subprocess.run(["hcitool", "name", mac], capture_output=True, text=True, timeout=5)
            return len(result.stdout.strip()) > 0
        except Exception:
            return False

    def calculate_r_axis(self):
        """
        Calcula el valor del Eje R (Relación) [cite: 74, 80]
        Móvil: Prioridad Alta (+5)
        PC/Watch: Prioridad Media (+2.5 cada uno)
        """
        r_value = 0
        
        # Prioridad Alta: Móvil (WiFi o BT)
        if self.scan_wifi(self.devices["PHONE_WIFI"]) or self.scan_bluetooth(self.devices["PHONE_BT"]):
            r_value += 5.0
            
        # Prioridad Media: PC
        if self.scan_wifi(self.devices["PC_NET"]):
            r_value += 2.5
            
        # Prioridad Media: Smartwatch
        if self.scan_bluetooth(self.devices["WATCH_BT"]):
            r_value += 2.5

        # Si no hay nadie, el eje tiende a negativo (soledad/vacío) [cite: 89, 93]
        return r_value if r_value > 0 else -5.0

    def run(self):
        while True:
            r_score = self.calculate_r_axis()
            self.mqtt.publish("orion/nsr/user/presence", r_score)
            time.sleep(15) # Escaneo cada 15 segundos para no saturar el bus

if __name__ == "__main__":
    sensor = PresenceSensor()
    sensor.run()