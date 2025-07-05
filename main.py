
import os
import time
import requests

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SEND_INTERVAL_SECONDS = 3600  # как часто отправлять сообщения (например, 1 раз в час)

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Failed to send message:", e)

if __name__ == "__main__":
    while True:
        send_telegram_message("✅ Привет, Толик! Это тестовое уведомление от ChatGPT 🤖")
        time.sleep(SEND_INTERVAL_SECONDS)
