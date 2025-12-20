import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from src.sensors.health import Homeostasis

load_dotenv("config/.env")

class OrionDiscord(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True # Vital para escuchar comandos
        super().__init__(command_prefix='/', intents=intents)
        self.channel_id = int(os.getenv("DISCORD_CHANNEL_ID"))

    async def on_ready(self):
        print(f"O.R.I.O.N. ha despertado como {self.user} (ID: {self.user.id})")
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send("🌌 **Sistemas inicializados.** A su servicio, Arquitecto. El NSR está bajo mi supervisión.")

    async def setup_hook(self):
        # Aquí registraremos futuros módulos de interacción
        pass

# Instancia del bot
bot_ds = OrionDiscord()

@bot_ds.command(name="status")
async def status(ctx):
    """Reporte de Homeostasis (Eje H)"""
    health = Homeostasis()
    m = health.monitor()
    
    # Mezcla de Cortana (humor/estilo) y Jarvis (eficiencia)
    embed = discord.Embed(
        title="🛰️ Reporte de Estado - NSR (Pi 4B)",
        description="Análisis de salud interna en tiempo real.",
        color=0x2ecc71 if m['status'] == "ESTABLE" else "0xe74c3c"
    )
    embed.add_field(name="Carga CPU", value=f"{m['cpu_load']}%", inline=True)
    embed.add_field(name="Temperatura", value=f"{m['temp']}°C", inline=True)
    embed.add_field(name="Eje H (Homeostasis)", value=m['status'], inline=False)
    
    # Un toque de sarcasmo elegante si la temperatura es alta
    footer_text = "Todo fluye según lo previsto." if m['temp'] < 60 else "El Músculo está algo tenso, Arquitecto. ¿Demasiada carga?"
    embed.set_footer(text=footer_text)
    
    await ctx.send(embed=embed)