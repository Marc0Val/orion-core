import telebot
import os
from dotenv import load_dotenv

load_dotenv("config/.env")

class OrionTelegram:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.bot = telebot.TeleBot(self.token)

    def send_message(self, text):
        try:
            self.bot.send_message(self.chat_id, text)
        except Exception as e:
            print(f"Error en Telegram: {e}")

# Instancia global para ser usada por el sistema
messenger_tg = OrionTelegram()