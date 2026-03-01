import json
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
source_channel = os.environ['SOURCE_DATA_CHANNEL']
target_channel = os.environ['TARGET_CHANNEL']
TOP_PAIRS = json.loads(os.environ['TOP_PAIRS'])
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
            matches = [
                item for item in TOP_PAIRS
                if item['name'].lower() in original_text.lower() and any(d.lower() in original_text.lower() for d in item['direction'])
            ]
            for ma in matches:
                logging.info(ma["name"])
                trade_time = re.search(r'(\b(?:[01]\d|2[0-3]):[0-5]\d\b)', modified_text, re.IGNORECASE)
                if trade_time:
                    tt = trade_time.group(1).strip()
                    dt_source = datetime.strptime(tt, "%H:%M").replace(tzinfo=tz_utc_minus_3)
                    dt_target = dt_source.astimezone(tz_utc_plus_5_30)
                    tt = f'{dt_target.strftime('%H:%M')}'
                    modified_text = modified_text + f"\nTIME: {tt} UTC+5:30"

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
