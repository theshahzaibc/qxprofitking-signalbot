import os
import re
import threading

import telethon
from telethon import TelegramClient, events
from dotenv import load_dotenv
from telethon import connection
from telethon.network import ConnectionTcpMTProxyIntermediate
from telethon.sessions import StringSession
import logging
from flask import Flask
from telethon.tl.functions.messages import CheckChatInviteRequest

# -------------------------------
# 1️⃣ START DUMMY FLASK WEB SERVER
# -------------------------------

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Telegram Bot is Running on Render!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Start Flask server in background
threading.Thread(target=run_web).start()


load_dotenv()
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
source_channel = os.environ['SOURCE_CHANNEL']
target_channel = os.environ['TARGET_CHANNEL']

proxy_host = os.getenv("HTTP_PROXY_HOST", None)
proxy_port = int(os.getenv("HTTP_PROXY_PORT", 0))
proxy_user = os.getenv("HTTP_PROXY_USER", None)
proxy_pass = os.getenv("HTTP_PROXY_PASS", None)
session_string = os.getenv("SESSION_STRING")


async def get_channel_id(client_, channel_link):
    invite_hash = channel_link.split("/")[-1]
    channel_id_ = None
    if "+" in channel_link:
        invite_hash = channel_link.split("/")[-1].replace("+", "")
        result = await client(CheckChatInviteRequest(invite_hash))
        channel_id_ = result.chat.id
    else:
        entity = await client_.get_entity(invite_hash)
        channel_id_ = entity.id
    if channel_id_:
        channel_id_ = int("-100{}".format(channel_id_))
    return channel_id_


logging.basicConfig(level=logging.INFO)


client = TelegramClient(StringSession(session_string), api_id, api_hash)
client.session.set_dc = lambda *args, **kwargs: None  # Prevents Telethon from writing to disk
client.session.save = lambda *args, **kwargs: None


async def main():
    await client.start()
    me = await client.get_me()
    print("Logged in as:", me.username or me.phone)
    target_channel_id = await get_channel_id(client, target_channel)
    source_channel_id = await get_channel_id(client, source_channel)
    print(target_channel_id)
    print(source_channel_id)

    @client.on(events.NewMessage(chats=source_channel_id))
    async def handler(event):
        try:
            # Forward the message
            if not event.message.message:
                return  # ignore non-text messages

            original_text = event.message.text
            modified_text = original_text.replace("https://broker-qx.pro/sign-up/?lid=652819", "https://market-qx.trade/en/sign-up?lid=1608650")
            modified_text = original_text.replace("https://broker-qx.pro/sign-up/?lid=1200739", "https://market-qx.trade/en/sign-up?lid=1608650")
            modified_text = original_text.replace("Masterguru", "QXPROFITKING")
            if len(modified_text) < 50:
                modified_text = modified_text + "\n\n\n━━━━━━━━━━━━━━━\n⚡ Powered By: QXProfitKing ⚡\n📩 Contact: @QuotexProfitKing"
            await client.send_message(target_channel_id, modified_text)
            print("Message forwarded:", modified_text)
        except Exception as e:
            print("Error:", e)
    print("🚀 Bot is running and waiting for messages...")
    await client.run_until_disconnected()  # ⬅️ KEEP LISTENING

with client:
    client.loop.run_until_complete(main())