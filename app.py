import os
import re
import threading
from telethon import TelegramClient, events
from dotenv import load_dotenv
from telethon.sessions import StringSession
import logging
import uvicorn
import asyncio
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from telethon.tl.functions.messages import CheckChatInviteRequest

from constants import SIGNAL_PAIR, SIGNAL_PAIR_ENT
from static import CALL_TRADE, CALL_TRADE_ENT, PUT_TRADE, PUT_TRADE_ENT, WIN_MSG, WIN_MSG_ENT, LOSS_MSG, LOSS_MSG_ENT

# -------------------------------
# 1️⃣ START DUMMY FLASK WEB SERVER
# -------------------------------

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def home():
    return "Bot is running successfully on Render!"


@app.api_route("/health", methods=["GET", "HEAD", "POST", "PUT"])
async def health_check():
    return {"status": "ok"}


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


async def extract_pair(text):
    import re

    # match USD/BRL, USD BRL, USDBRL
    m = re.search(r'\b([A-Z]{3})[\/\-\s]?([A-Z]{3})\b', text.upper())
    if not m:
        return None

    c1, c2 = m.group(1), m.group(2)

    direct = f"{c1}/{c2}"
    return direct


logging.basicConfig(level=logging.INFO)

client = TelegramClient(StringSession(session_string), api_id, api_hash)
client.session.set_dc = lambda *args, **kwargs: None  # Prevents Telethon from writing to disk
client.session.save = lambda *args, **kwargs: None

tz_utc_minus_3 = timezone(timedelta(hours=-3))
tz_utc_plus_5_30 = timezone(timedelta(hours=5, minutes=30))


async def telethon_main():
    await client.connect()
    logging.info("📡 Connected to Telegram...")
    if not await client.is_user_authorized():
        logging.error("❌ ERROR: SESSION_STRING invalid or expired.")
        return
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
            ent_m = None
            if event.entities:
                ent_m = event.entities

            # Forward the message
            if not event.message.message:
                return  # ignore non-text messages

            original_text = event.message.text
            modified_text = original_text
            modified_text = re.sub(r"(\?lid=)\d+", rf"{REF_URL}", original_text)
            modified_text = modified_text.replace("Masterguru", "QXPROFITKING")
            modified_text = modified_text.replace("@Binnerytrader", "@QuotexProfitKing")
            modified_text = modified_text.replace("𝑸𝑼𝑶𝑻𝑬𝑿 𝑮𝑼𝑹𝑼", "QXProfitKing")
            modified_text = modified_text.replace("𝗤𝘂𝗼𝘁𝗲𝘅 𝗚𝘂𝗿𝘂", "QXProfitKing")
            modified_text = modified_text + "\n\n CREATE YOUR ACCOUNT NOW\n{}\n\n".format(REF_URL)
            if "FreeSignals_Trading" in source_channel:
                modified_text = modified_text + "\n━━━━━━━━━━━━━━━\n⚡ Powered By: QXProfitKing ⚡\n📩 Contact: @QuotexProfitKing"

            pair = re.search(r'\b([A-Z]{3})[\/\-\s]?([A-Z]{3})\b', original_text.upper())
            cc = ""
            if pair and not ("Profit" in original_text):
                try:
                    cc = await extract_pair(original_text)
                    if cc:
                        cc = cc.strip() + " OTC" if "OTC" in original_text.upper() else cc.strip() + " LIV"
                        trade_time = re.search(r'(\b(?:[01]\d|2[0-3]):[0-5]\d\b)', modified_text, re.IGNORECASE)
                        tt = trade_time.group(1).strip()
                        dt_source = datetime.strptime(tt, "%H:%M").replace(tzinfo=tz_utc_minus_3)
                        dt_target = dt_source.astimezone(tz_utc_plus_5_30)
                        tt = f'{dt_target.strftime('%H:%M')}'
                        trade_direction = re.search(r'(\b(?:put|call)\b)', modified_text.lower(), re.IGNORECASE)
                        trade_direction = trade_direction.group(1)
                        if "call" in trade_direction.lower():
                            modified_text = CALL_TRADE.format(cc.upper(), tt)
                            ent_m = CALL_TRADE_ENT
                        if "put" in trade_direction.lower():
                            modified_text = PUT_TRADE.format(cc.upper(), tt)
                            ent_m = PUT_TRADE_ENT
                except:
                    pass

            logging.info(original_text)
            if "Profit" in original_text:
                modified_text = WIN_MSG
                ent_m = WIN_MSG_ENT
            if "Loss" in original_text:
                modified_text = LOSS_MSG
                ent_m = LOSS_MSG_ENT

            await client.send_message(
                target_channel_id,
                modified_text,
                formatting_entities=ent_m,
                link_preview=False
            )
            logging.info("Message forwarded")
        except Exception as e:
            logging.error("Error: {}".format(str(e)))

    logging.info("🚀 Bot is running and waiting for messages...")
    await client.run_until_disconnected()  # ⬅️ KEEP LISTENING


def start_telethon():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(telethon_main())


if __name__ == "__main__":
    # Start Telethon bot in a background thread
    threading.Thread(target=start_telethon, daemon=True).start()

    # Start FastAPI server on Render's assigned PORT
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
