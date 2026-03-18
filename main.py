from telethon import TelegramClient, events
import re
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

channel = os.getenv("CHANNEL")

def parse_signal(text):
    signal = {}

    if "BUY" in text.upper():
        signal["type"] = "buy"
    elif "SELL" in text.upper():
        signal["type"] = "sell"

    match = re.search(r"[A-Z]{3,6}", text)
    if match:
        signal["symbol"] = match.group()

    match = re.search(r"\d+\.\d+", text)
    if match:
        signal["lot"] = float(match.group())

    match = re.search(r"SL\s*(\d+)", text)
    if match:
        signal["sl"] = int(match.group(1))

    match = re.search(r"TP\s*(\d+)", text)
    if match:
        signal["tp"] = int(match.group(1))

    return signal


@client.on(events.NewMessage(chats=channel))
async def handler(event):
    text = event.text
    print("SIGNAL:", text)

    parsed = parse_signal(text)
    print("PARSED:", parsed)


client.start()
print("BOT LIVE 🚀")

client.run_until_disconnected()
