import asyncio
import os
import time
from dotenv import load_dotenv
from src.sensors.health import Homeostasis
from src.messengers.telegram_bot import messenger_tg
from src.messengers.discord_bot import bot_ds

# Cargamos configuración desde el .env [cite: 198]
load_dotenv("config/.env")

async def startup_sequence():
    """
    Secuencia de inicio: Reporta salud inicial y despierta el bot de Discord.
    """
    # 1. Análisis de Homeostasis (Eje H) [cite: 60, 62]
    health = Homeostasis()
    metrics = health.monitor()
    
    # 2. Construcción del mensaje de O.R.I.O.N. [cite: 1, 22]
    # Mezcla de elegancia (Jarvis) e ingenio (Cortana) [cite: 2, 29]
    msg = (
        f"🌌 **O.R.I.O.N. Online**\n"
        f"Arquitecto, los sistemas en el NSR están operativos. [cite: 30, 45]\n\n"
        f"📊 **Estado de Homeostasis (Eje H):** [cite: 62]\n"
        f"- CPU: {metrics['cpu_load']}%\n"
        f"- Temp: {metrics['temp']}°C\n"
        f"- Status: {metrics['status']}\n\n"
        f"Esperando instrucciones en el canal de mando. [cite: 23]"
    )
    
    # 3. Notificación vía Telegram (Síncrono)
    try:
        messenger_tg.send_message(msg)
    except Exception as e:
        print(f"Error al enviar pulso a Telegram: {e}")

    # 4. Ejecución del Bot de Discord (Asíncrono)
    # Este proceso es bloqueante, mantendrá vivo el contenedor [cite: 173, 180]
    async with bot_ds:
        token = os.getenv("DISCORD_TOKEN")
        await bot_ds.start(token)

if __name__ == "__main__":
    try:
        # Iniciamos el bucle de eventos asíncrono [cite: 51]
        asyncio.run(startup_sequence())
    except KeyboardInterrupt:
        # Mi lado Jarvis: Una retirada impecable [cite: 25, 34]
        print("\n[!] O.R.I.O.N. entrando en modo hibernación... A su servicio, Señor.")