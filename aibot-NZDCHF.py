import asyncio
import os
import time

# import socks
from telethon import TelegramClient, events
from dotenv import load_dotenv
import logging

from telethon.errors import SessionPasswordNeededError
from telethon.sessions import StringSession
from telethon.tl.functions.messages import CheckChatInviteRequest

load_dotenv()
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
source_channel = os.environ['SOURCE_CHANNEL_AI']
target_channel = os.environ['TARGET_NZDCHF_BOT']
phone_number = os.environ['PHONE_NUM']
password = os.getenv("TELEGRAM_PASSWORD")

proxy_host = os.getenv("HTTP_PROXY_HOST", None)
proxy_port = int(os.getenv("HTTP_PROXY_PORT", 0))
proxy_user = os.getenv("HTTP_PROXY_USER", None)
proxy_pass = os.getenv("HTTP_PROXY_PASS", None)


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


async def wait_for_code():
    """Poll environment until CODE is available."""
    code = os.getenv("CODE")
    while not code:
        print("⏳ Waiting for CODE environment variable...")
        time.sleep(5)
        load_dotenv(override=True)  # refresh .env if updated
        code = os.getenv("CODE")
    print(f"✅ Code found: {code}")
    return code


# if proxy_user and proxy_pass:
#     proxy = (socks.SOCKS5, proxy_host, proxy_port, True, proxy_user, proxy_pass)
# else:
#     proxy = ('http', proxy_host, proxy_port)

logging.basicConfig(level=logging.INFO)

client = TelegramClient('client_session', api_id, api_hash)


async def main():
    await client.connect()
    print("📡 Connected to Telegram...")
    if not await client.is_user_authorized():
        print("sending code to: {}".format(phone_number))
        await client.send_code_request(phone_number)
        code = await wait_for_code()
        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            print("🔐 2FA enabled — signing in with password...")
            await client.sign_in(password=password)
    else:
        print("🔓 Already authorized.")
    me = await client.get_me()
    logging.info("Logged in as: {}".format(me.username))
    target_channel_id = await get_channel_id(client, target_channel)
    source_channel_id = await get_channel_id(client, source_channel)

    # -1002765478569 source channel

    @client.on(events.NewMessage(chats=source_channel_id))
    async def handler(event):
        try:
            # Forward the message
            if not event.message.message:
                return  # ignore non-text messages

            original_text = event.message.text
            if "NZDCHF-OTC" in original_text or "USDARS-OTC" in original_text:
                modified_text = "---------------\nSPECIAL CHANNEL SIGNAL\n---------------\n" + original_text
                modified_text = modified_text.replace("@Binnerytrader", "@QuotexProfitKing")
                modified_text = modified_text.replace("𝑸𝑼𝑶𝑻𝑬𝑿 𝑮𝑼𝑹𝑼", "QXProfitKing")
                modified_text = modified_text.replace("𝗤𝘂𝗼𝘁𝗲𝘅 𝗚𝘂𝗿𝘂", "QXProfitKing")
                await client.send_message(target_channel_id, modified_text)
                logging.info("Signal send to channel.{}".format(modified_text))
        except Exception as e:
            logging.error(str(e))

    logging.info("🚀 Bot is running and waiting for messages...")
    await client.run_until_disconnected()  # ⬅️ KEEP LISTENING


if __name__ == "__main__":
    asyncio.run(main())
