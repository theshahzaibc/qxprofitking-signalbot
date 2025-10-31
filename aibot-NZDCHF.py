import os
# import socks
from telethon import TelegramClient, events
from dotenv import load_dotenv
import logging

from telethon.tl.functions.messages import CheckChatInviteRequest

load_dotenv()
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
source_channel = os.environ['SOURCE_CHANNEL_AI']
target_channel = os.environ['TARGET_NZDCHF_BOT']

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


# if proxy_user and proxy_pass:
#     proxy = (socks.SOCKS5, proxy_host, proxy_port, True, proxy_user, proxy_pass)
# else:
#     proxy = ('http', proxy_host, proxy_port)

logging.basicConfig(level=logging.INFO)

client = TelegramClient('http_session', api_id, api_hash)


async def main():
    await client.start()
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


with client:
    client.loop.run_until_complete(main())
