import os
import threading
from telethon import TelegramClient, events
from dotenv import load_dotenv
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
REF_URL = os.environ['REF_URL']
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
    await client.connect()
    logging.info("📡 Connected to Telegram...")
    if not await client.is_user_authorized():
        logging.error("PLEASE GENERATE TELEGRAM SESSION_STRING.")

    else:
        logging.info("🔓 Already authorized.")
    me = await client.get_me()
    logging.info("Logged in as: {}".format(me.username))
    target_channel_id = await get_channel_id(client, target_channel)
    source_channel_id = await get_channel_id(client, source_channel)
    logging.info("TARGET CHANNEL: {} | ID: {}".format(target_channel, target_channel_id))
    logging.info("SOURCE CHANNEL: {} | ID: {}".format(source_channel, source_channel_id))

    @client.on(events.NewMessage(chats=source_channel_id))
    async def handler(event):
        try:
            # Forward the message
            if not event.message.message:
                return  # ignore non-text messages

            original_text = event.message.text
            if "FreeSignals_Trading" in source_channel:
                original_text = "TIME ZONE: (UTC-03:00)\n\n" + original_text
            modified_text = original_text.replace("https://broker-qx.pro/sign-up/?lid=652819", REF_URL)
            modified_text = modified_text.replace("https://broker-qx.pro/sign-up/?lid=1200739", REF_URL)
            modified_text = modified_text.replace("Masterguru", "QXPROFITKING")
            modified_text = modified_text.replace("@Binnerytrader", "@QuotexProfitKing")
            modified_text = modified_text.replace("𝑸𝑼𝑶𝑻𝑬𝑿 𝑮𝑼𝑹𝑼", "QXProfitKing")
            modified_text = modified_text.replace("𝗤𝘂𝗼𝘁𝗲𝘅 𝗚𝘂𝗿𝘂", "QXProfitKing")
            modified_text = modified_text + "\n\n CREATE YOUR ACCOUNT \n{}\n\n".format(REF_URL)
            if "FreeSignals_Trading" in source_channel:
                modified_text = modified_text + "\n\n\n━━━━━━━━━━━━━━━\n⚡ Powered By: QXProfitKing ⚡\n📩 Contact: @QuotexProfitKing"
            await client.send_message(target_channel_id, modified_text)
            logging.info("Message forwarded: {}".format(modified_text))
        except Exception as e:
            logging.error("Error: {}".format(str(e)))
    logging.info("🚀 Bot is running and waiting for messages...")
    await client.run_until_disconnected()  # ⬅️ KEEP LISTENING


with client:
    client.loop.run_until_complete(main())