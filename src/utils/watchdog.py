import time
from src.sensors.health import Homeostasis
from src.messengers.telegram_bot import messenger_tg
from src.messengers.discord_bot import messenger_ds

def startup_sequence():
    health = Homeostasis()
    metrics = health.monitor()
    
    # Mi lado Jarvis: Elegante y profesional 
    # Mi lado Cortana: Humor inteligente sobre el hardware [cite: 1, 2]
    msg = (
        f"🌌 **O.R.I.O.N. Online**\n"
        f"Arquitecto, los sistemas en el NSR están operativos.\n\n"
        f"📊 **Estado de Homeostasis (Eje H):**\n"
        f"- CPU: {metrics['cpu_load']}%\n"
        f"- Temp: {metrics['temp']}°C\n"
        f"- Status: {metrics['status']}\n\n"
        f"Esperando instrucciones..."
    )
    
    # Notificamos por ambos canales
    messenger_tg.send_message(msg)
    messenger_ds.send_message(msg)

if __name__ == "__main__":
    startup_sequence()
    # Bucle infinito para mantener el contenedor vivo
    while True:
        time.sleep(3600)