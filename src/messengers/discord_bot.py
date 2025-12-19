import requests
import os
from dotenv import load_dotenv

load_dotenv("config/.env")

class OrionDiscord:
    def __init__(self):
        self.token = os.getenv("DISCORD_TOKEN")
        self.channel_id = os.getenv("DISCORD_CHANNEL_ID")
        self.base_url = f"https://discord.com/api/v9/channels/{self.channel_id}/messages"
        self.headers = {"Authorization": f"Bot {self.token}"}

    def send_message(self, content):
        # Usamos Web API para evitar mantener una conexión persistente pesada en esta fase
        payload = {"content": content}
        try:
            res = requests.post(self.base_url, json=payload, headers=self.headers)
            return res.status_code == 200
        except Exception as e:
            print(f"Error en Discord: {e}")
            return False

messenger_ds = OrionDiscord()