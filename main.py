from telethon import TelegramClient, events
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print("Yangi signal:", event.text)

client.start()
print("Telegram bot ishlayapti 🚀")

client.run_until_disconnected()
