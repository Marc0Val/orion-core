import psutil
import time
import os

class Homeostasis:
    """Módulo encargado de la salud interna del hardware (Eje H) """
    
    def get_cpu_usage(self):
        # Retorna el porcentaje de carga de CPU [cite: 65]
        return psutil.cpu_percent(interval=1)

    def get_temperature(self):
        # Lee la temperatura del procesador de la Pi 4 [cite: 66]
        try:
            temp = os.popen("vcgencmd measure_temp").readline()
            return float(temp.replace("temp=", "").replace("'C\n", ""))
        except Exception:
            return 0.0

    def monitor(self):
        cpu = self.get_cpu_usage()
        temp = self.get_temperature()
        # Lógica de autodiagnóstico: Si la temp > 75°C, el Eje H entra en modo crítico [cite: 91, 120]
        status = "ESTABLE" if temp < 70 else "CRÍTICO"
        return {"cpu_load": cpu, "temp": temp, "status": status}

if __name__ == "__main__":
    h = Homeostasis()
    while True:
        print(f"O.R.I.O.N. Health Check: {h.monitor()}")
        time.sleep(10)