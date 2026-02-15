import os
import random
import re
from datetime import datetime, timedelta, timezone
from telethon import TelegramClient, events
from dotenv import load_dotenv
from telethon.helpers import add_surrogate
from telethon.sessions import StringSession
import logging
import asyncio
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from telethon.tl.functions.messages import CheckChatInviteRequest, GetStickerSetRequest, SendMultiMediaRequest
from telethon.tl.types import InputStickerSetShortName, InputDocument

from constants import *

app = FastAPI()

UTC_PLUS_530 = timezone(timedelta(hours=5, minutes=30))


@app.get("/", response_class=PlainTextResponse)
async def home():
    return "Bot is running successfully on T_KING_VIP!"


@app.api_route("/health", methods=["GET", "HEAD", "POST", "PUT"])
async def health_check():
    return {"status": "OK"}


load_dotenv()
api_id = int(os.environ['TELEGRAM_API_ID'])
api_hash = os.environ['TELEGRAM_API_HASH']
source_channel = os.environ['SOURCE_CHANNEL_KING_VIP']
target_channel = os.environ['PUBLIC_TARGET_CHANNEL']
REF_URL = os.environ['REF_URL']

session_string = os.getenv("SESSION_STRING")
SESSION_START_ID = [6260306930074393118, 1032603446122905641]
SESSION_CLOSE_ID = [6260074022587866684, 1032603446122905642]
session_active = True
forwarded_albums = set()
album_locks = {}
message_map = {}
sent_stickers_for_msg = {}

SHOTS_HASH_TAG = [
    "#SURESHOT_WIN_PROFITKING ❤️🫶",
    "#WIN_PROFITKING ❤️🫶",
    "#DEEP_WIN_SURESHOT_PROFITKING ❤️🫶",
    "#DEEP_WIN_PROFITKING ❤️🫶",
    "#DEEP_DIRECT_WIN_PROFITKING ❤️🫶",
    "#ROCKET_WIN_PROFITKING ❤️🫶❤️🫶",
    "#ROCKET_SURESHOT_PROFITKING ❤️🫶",
]

SHOTS_HASH_TAG_keywords = [
    "DIRECT",
    "SURESHOT",
    "ONE_MORE",
    "BACK_TO_BACK",
    "PROFITABLE",
    "ITM",
    "ROCKET",
    "DIRECTSHOT",
    "DEEP",
    "POWEROFTRADINGKING",
    "ONE_MORE_WON"
]

pattern = r"(" + "|".join(map(re.escape, SHOTS_HASH_TAG_keywords)) + ")"
media_text_regex = re.compile(pattern, re.IGNORECASE)

SESSION_SOON_PATTERN = re.compile(
    r"(session.*(soon|starting|start|conducted|in\s*\d+\s*(min|minute|minutes|hr|hour))"
    r"|be\s+ready|Ready\s+For\s+Session)",
    re.IGNORECASE
)

VALID_OTC_PAIRS = {
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD", "USD/CAD", "NZD/USD",
    "EUR/GBP", "EUR/JPY", "GBP/JPY", "EUR/CHF", "GBP/CHF", "AUD/JPY", "CAD/JPY", "CHF/JPY",
    "USD/BRL", "USD/BDT", "USD/ARS", "USD/INR", "USD/PKR", "USD/TRY", "USD/IDR",
    "USD/NGN", "USD/MXN", "USD/CLP", "USD/COP", "USD/EGP", "USD/VND", "USD/THB",
    "USD/MYR", "USD/PHP", "USD/KZT", "USD/AED", "USD/SAR", "USD/QAR", "USD/KWD", "USD/BHD", "AUD/CHF"
}


async def extract_pair(text):
    import re

    # match USD/BRL, USD BRL, USDBRL
    m = re.search(r'\b([A-Z]{3})[\/\-\s]?([A-Z]{3})\b', text.upper())
    if not m:
        return None

    c1, c2 = m.group(1), m.group(2)

    direct = f"{c1}/{c2}"
    reverse = f"{c2}/{c1}"

    if direct in VALID_OTC_PAIRS:
        return direct
    if reverse in VALID_OTC_PAIRS:
        return reverse

    return None


async def clean_text(text_content):
    modified_text = text_content
    try:
        modified_text = modified_text.replace("T.KING", "PROFIT KING")
        modified_text = modified_text.replace("TRADING KING", "PROFIT KING")
        modified_text = modified_text.replace("TRADINGKING", "PROFIT KING")
        modified_text = modified_text.replace("TRADING_KING", "PROFIT KING")
        modified_text = re.sub(r"(\?lid=)\d+", rf"{REF_URL}", modified_text)
        modified_text = modified_text.replace("@kingtraderpersonal", "@QuotexProfitKing")
        if text_content.startswith("**") and text_content.endswith("**"):
            modified_text = text_content[2:-2]
        if "**" in text_content:
            modified_text = text_content.replace("**", "")

    except:
        logging.exception("An clean_text() exception was thrown!")

    return modified_text


async def forward_album(event, modified_text, target_channel_id, source_channel_id):
    try:
        """Forward media albums safely (single message)"""
        grouped_id = getattr(event, "grouped_id", None)
        if not grouped_id or grouped_id in forwarded_albums:
            return

        lock = album_locks.setdefault(grouped_id, asyncio.Lock())
        async with lock:
            if grouped_id in forwarded_albums:
                return

            # fetch recent messages (enough to cover the album)
            messages = await client.get_messages(source_channel_id, limit=50)
            album_msgs = [m for m in messages if getattr(m, "grouped_id", None) == grouped_id]
            album_msgs.sort(key=lambda m: m.id or 0)

            if not album_msgs:
                return

            files = []
            for msg in album_msgs:
                if msg.photo:
                    files.append(msg.photo)
                elif msg.document:
                    files.append(msg.document)

            # caption from first text
            caption = None
            caption_entities = None
            for msg in album_msgs:
                if msg.text:
                    caption = await clean_text(msg.text)
                    break
            ent_m = event.entities

            if media_text_regex.search(caption):
                caption = random.choice(SHOTS_HASH_TAG)
            if "@AJAYTRADER43" in caption:
                caption = caption.replace("@AJAYTRADER43", "@QuotexProfitKing")
                caption = caption.replace("@AJAYTRADER43".lower(), "@QuotexProfitKing")
                try:
                    safe_word = add_surrogate("@QuotexProfitKing")
                    safe_text = add_surrogate(caption)
                    offset = safe_text.find("@QuotexProfitKing")
                    mtt = caption.split("@QuotexProfitKing")
                    caption = mtt[0] + "@QuotexProfitKing✅" + mtt[-1]
                    ent_m.append(
                        MessageEntityCustomEmoji(
                            offset=offset + len(safe_word),
                            length=1,
                            document_id=4985790168263820344
                        )
                    )
                except:
                    logging.exception("An exception was thrown!")
            logging.info(caption)
            sent_msgs = await client.send_file(
                target_channel_id,
                files,
                caption=caption,
                caption_entities=ent_m
            )
            forwarded_albums.add(grouped_id)
            for src_msg, dest_msg in zip(album_msgs, sent_msgs):
                message_map[(event.chat_id, src_msg.id)] = dest_msg.id
    except:
        logging.exception("An exception was thrown!")


async def replace_username(mf_text):
    res = {'mft': "", "ent_m": None}
    mf_text = mf_text.replace("@kingtraderpersonal", "@QuotexProfitKing")
    if "@QuotexProfitKing" in mf_text:
        try:
            safe_word = add_surrogate("@QuotexProfitKing")
            safe_text = add_surrogate(mf_text)
            offset = safe_text.find("@QuotexProfitKing")
            mtt = mf_text.split("@QuotexProfitKing")
            mf_text = mtt[0] + "@QuotexProfitKing✅" + mtt[-1]
            res['mft'] = mf_text
            res['ent_m'] = MessageEntityCustomEmoji(
                offset=offset + len(safe_word),
                length=1,
                document_id=4985790168263820344
            )
        except:
            logging.exception("An exception was thrown!")

    return res


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
client.session.set_dc = lambda *args, **kwargs: None
client.session.save = lambda *args, **kwargs: None


async def telethon_main():
    global session_active
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

    if len(message_map) > 100:
        message_map.clear()

    @client.on(events.MessageDeleted(chats=source_channel_id))
    async def on_message_deleted(event):
        for msg_id in event.deleted_ids:
            if msg_id in sent_stickers_for_msg:
                sticker_ids = sent_stickers_for_msg[msg_id]
                # Delete sent sticker messages from destination
                await client.delete_messages(target_channel_id, sticker_ids)
                # Remove from tracking
                del sent_stickers_for_msg[msg_id]

            key = (event.chat_id, msg_id)

            dest_msg_id = message_map.get(key)
            if not dest_msg_id:
                continue

            await client.delete_messages(
                target_channel_id,
                dest_msg_id
            )

            # Cleanup
            del message_map[key]

    @client.on(events.NewMessage(chats=source_channel_id))
    async def handler(event):
        global session_active
        msg = event.message

        STICKERS_MAP = {
            "6260306930074393118": {"use": "START", "hash": "5541015946990930482", "id": "5769185348286421680"},
            "6260074022587866684": {"use": "CLOSE", "hash": "1677306580397481331", "id": "5769523456701899198"},
            "6260221322786249195": {"use": "UP", "hash": "6411712796155122903", "id": "5769329156676395099"},
            "6260186220018539705": {"use": "DOWN", "hash": "7689131038073084631", "id": "5769203241120178254"},
            "6260514681937472453": {"use": "WIN", "hash": "739291283228231660", "id": "5769587773837155090"},
            "6260438029656135735": {"use": "WIN", "hash": "739291283228231660", "id": "5769587773837155090"},
            "1032603446122905641": {"use": "START", "hash": "5541015946990930482", "id": "5769185348286421680"},
            "1032603446122905642": {"use": "CLOSE", "hash": "1677306580397481331", "id": "5769523456701899198"},
            "1032603446122905607": {"use": "UP", "hash": "6411712796155122903", "id": "5769329156676395099"},
            "1032603446122905606": {"use": "DOWN", "hash": "7689131038073084631", "id": "5769203241120178254"},
            "1032603446122905608": {"use": "WIN", "hash": "739291283228231660", "id": "5769587773837155090"}
        }
        try:

            if "NO SESSION" in msg.text:
                NoSession = ""
                ent_m = []
                sent = await client.send_message(
                    target_channel_id,
                    NoSession,
                    formatting_entities=ent_m,
                    link_preview=False
                )
                message_map[(event.chat_id, event.id)] = sent.id
                return

                # logging.info(event.message)
            sticker_set = await client(
                GetStickerSetRequest(
                    stickerset=InputStickerSetShortName("profitkingsignals"),
                    hash=0
                )
            )

            sticker_wins = [
                {"id": 2237606192312483841, "hash": 4033837751369202276},
                {"id": 2237606192312483848, "hash": -3778415565738156827},
                {"id": 2237606192312483854, "hash": 7890136828345908544},
                {"id": 6334790257216590047, "hash": 3498491783387742290},
                {"id": 6334651078801363297, "hash": 9086096481231876058},
                {"id": 6334371974646601009, "hash": -203118863801637991},
                {"id": 6336971172890022960, "hash": -6490575582558450301},
                {"id": 6334589330056548983, "hash": 4090714155318049382},
                {"id": 6334642205398930168, "hash": -7528692251810447384}
            ]
            # if event.entities:
            #     for ent in event.entities:
            #         logging.info(ent)

            # logging.info(event)

            original_text = event.message.text
            if original_text == "1 MINUTE EXPIRY":
                return
            msgs = []
            session_start = SESSION_SOON_PATTERN.search(original_text)
            if session_start:
                try:
                    msgs = [
                        {
                            'text': PUBLIC_SESSION_GR,
                            'ent': GR_ENT
                        }
                    ]
                except:
                    logging.exception("An exception was thrown!")
            if msgs:
                try:
                    for msg in msgs:
                        if msg['text']:
                            sent = await client.send_message(target_channel_id, msg['text'],
                                                             formatting_entities=msg['ent'])
                            message_map[(event.chat_id, event.id)] = sent.id
                except:
                    logging.exception("An exception was thrown!")

            if ("Ready" in original_text or "Readyy..." in original_text) and not session_active:
                session_active = True
                logging.info("READY TYUE")
                try:
                    for doc in sticker_set.documents:
                        if str(doc.id) == "5769185348286421680":
                            input_doc = InputDocument(
                                id=doc.id,
                                access_hash=doc.access_hash,
                                file_reference=doc.file_reference
                            )

                            sent = await client.send_file(
                                target_channel_id,
                                input_doc
                            )
                            message_map[(event.chat_id, event.id)] = sent.id
                            break
                except Exception as e:
                    logging.exception("An exception was thrown!")
                logging.info("SESSION STARTED!")
                return

            if (getattr(msg, "sticker", None) and msg.sticker.id in SESSION_START_ID) and not session_active:
                msg_sticker = msg.sticker
                logging.info("SID {}".format(msg_sticker.id))
                session_active = True
                try:
                    if msg_sticker.id:
                        STICKER_ = STICKERS_MAP[str(msg_sticker.id)]

                        for doc in sticker_set.documents:
                            if str(doc.id) == STICKER_['id']:
                                input_doc = InputDocument(
                                    id=doc.id,
                                    access_hash=doc.access_hash,
                                    file_reference=doc.file_reference
                                )

                                sent = await client.send_file(
                                    target_channel_id,
                                    input_doc
                                )
                                message_map[(event.chat_id, event.id)] = sent.id
                                break
                except Exception as e:
                    logging.exception("An exception was thrown!")
                    logging.info("NOT  STICKER")
                logging.info("SESSION STARTED!")
                return
            if "No Feadbacks No Session" in original_text and session_active:
                session_active = False
                try:
                    for doc in sticker_set.documents:
                        if str(doc.id) == "5769523456701899198":
                            input_doc = InputDocument(
                                id=doc.id,
                                access_hash=doc.access_hash,
                                file_reference=doc.file_reference
                            )

                            sent = await client.send_file(
                                target_channel_id,
                                input_doc
                            )
                            message_map[(event.chat_id, event.id)] = sent.id
                            break
                except Exception as e:
                    logging.exception("An exception was thrown!")
                logging.info("SESSION CLOSED!")
                return
            if (getattr(msg, "sticker",
                        None) and msg.sticker.id in SESSION_CLOSE_ID) and session_active:
                msg_sticker = msg.sticker
                logging.info("SID {}".format(msg_sticker.id))
                session_active = False
                try:
                    if msg_sticker.id:
                        STICKER_ = STICKERS_MAP[str(msg_sticker.id)]

                        for doc in sticker_set.documents:
                            if str(doc.id) == STICKER_['id']:
                                input_doc = InputDocument(
                                    id=doc.id,
                                    access_hash=doc.access_hash,
                                    file_reference=doc.file_reference
                                )

                                sent = await client.send_file(
                                    target_channel_id,
                                    input_doc
                                )
                                message_map[(event.chat_id, event.id)] = sent.id
                                break
                except Exception as e:
                    logging.exception("An exception was thrown!")
                    logging.info("NOT  STICKER")
                logging.info("SESSION CLOSED!")
                return

            if not session_active:
                logging.info("MESSAGE OUTSIDE SESSION!")

            msg = event.message
            modified_text = original_text
            modified_text = await clean_text(modified_text)
            if "youtube.com" in modified_text or "youtu.be" in modified_text or "t.me" in modified_text or "Live Stream".lower() in modified_text.lower():
                return
            if session_active:

                if getattr(msg, "sticker", None):
                    logging.info("STICKER")
                    if msg.sticker.id in SESSION_START_ID or msg.sticker.id in SESSION_CLOSE_ID:
                        logging.info("ALREADY SESSION")
                        return
                    msg_sticker = msg.sticker
                    logging.info("SID {}".format(msg_sticker.id))
                    logging.info("SHAS {}".format(msg_sticker.access_hash))
                    try:
                        if msg_sticker.id:
                            STICKER_ = STICKERS_MAP[str(msg_sticker.id)]
                            if STICKER_['use'] == "WIN":
                                logging.info("WIN")
                                SURE_SHOT_MSG = SURESHOT
                                ent_m_2 = SURESHOT_ENT
                                selected_stickers = random.sample(sticker_wins, 2)
                                sent_msgs = []
                                for s in selected_stickers:
                                    doc = InputDocument(id=s["id"], access_hash=s["hash"], file_reference=b'')
                                    sent = await client.send_file(
                                        target_channel_id,
                                        doc
                                    )
                                    sent_msgs.append(sent)
                                sent_TEXT = await client.send_message(
                                    target_channel_id,
                                    SURE_SHOT_MSG,
                                    formatting_entities=ent_m_2,
                                    link_preview=False
                                )
                                sent_msgs.append(sent_TEXT)
                                if not isinstance(sent_msgs, list):
                                    sent_msgs = [sent_msgs]

                                    # Track sent sticker message IDs
                                sent_stickers_for_msg[event.id] = [m.id for m in sent_msgs]
                            for doc in sticker_set.documents:
                                if str(doc.id) == STICKER_['id']:
                                    input_doc = InputDocument(
                                        id=doc.id,
                                        access_hash=doc.access_hash,
                                        file_reference=doc.file_reference
                                    )

                                    sent = await client.send_file(
                                        target_channel_id,
                                        input_doc
                                    )
                                    message_map[(event.chat_id, event.id)] = sent.id
                                    break
                    except Exception as e:
                        sent = await client.send_file(
                            target_channel_id,
                            msg.sticker
                        )
                        message_map[(event.chat_id, event.id)] = sent.id
                elif getattr(event, "grouped_id", None):
                    logging.info("group")
                    await forward_album(event, modified_text=modified_text, target_channel_id=target_channel_id,
                                        source_channel_id=source_channel_id)
                    return
                elif getattr(msg, "media", None):
                    logging.info("media")
                    ent_m = event.entities
                    if media_text_regex.search(modified_text):
                        modified_text = random.choice(SHOTS_HASH_TAG)

                    if "@kingtraderpersonal".lower() in modified_text.lower():
                        r_username = await replace_username(modified_text)
                        if r_username:
                            modified_text = r_username['mft']
                            ent_m.append(r_username['ent_m'])
                    sent = await client.send_file(
                        target_channel_id,
                        msg.media,
                        caption=modified_text,
                        formatting_entities=ent_m
                    )
                    message_map[(event.chat_id, event.id)] = sent.id
                else:
                    logging.info("text")
                    ent_m = event.entities
                    pair = re.search(r'\b([A-Z]{3})[\/\-\s]?([A-Z]{3})\b', modified_text.upper())
                    if pair:
                        cc = ""
                        try:
                            cc = await extract_pair(modified_text)
                        except:
                            pass
                        if cc:
                            cc = cc.strip() + " OTC" if "OTC" in modified_text.upper() else cc.strip() + " LIV"
                            modified_text = SIGNAL_PAIR.format(cc.upper())
                            ent_m = SIGNAL_PAIR_ENT
                    if "@kingtraderpersonal".lower() in original_text.lower():
                        r_username = await replace_username(modified_text)
                        if r_username:
                            modified_text = r_username['mft']
                            ent_m.append(r_username['ent_m'])

                    if "SEND FEADBACKS" in original_text or "Post par jldi se" in original_text or "200 reactions krwado" in original_text or "NEXT SIGNAL" in original_text.upper() or "reaction hojayga" in original_text.upper() or "REACTION" in original_text.upper():
                        modified_text = FEEDBACK_MSG
                        ent_m = FEEDBACK_MSG_ENT

                    if "Readyy ???" in original_text or "are you ready" in original_text or "Ready ???" in original_text or "Readyy..." in original_text or "Ready..." in original_text:
                        modified_text = REACTIONS
                        ent_m = REACTIONS_ENT

                    if "700000000000001" in original_text:
                        modified_text = SURESHOT
                        ent_m = SURESHOT_ENT
                        selected_stickers = random.sample(sticker_wins, 2)
                        sent_msgs = []
                        for s in selected_stickers:
                            doc = InputDocument(id=s["id"], access_hash=s["hash"], file_reference=b'')
                            sent = await client.send_file(
                                target_channel_id,
                                doc
                            )
                            sent_msgs.append(sent)

                        if not isinstance(sent_msgs, list):
                            sent_msgs = [sent_msgs]

                            # Track sent sticker message IDs
                        sent_stickers_for_msg[event.id] = [m.id for m in sent_msgs]

                    if "Want 1 more sureshot like this?" in original_text:
                        modified_text = WANT_MORE
                        ent_m = WANT_MORE_ENT

                    BACK_WINS_MSG = re.search(r"Back to back\s+(\d+)\s+(.*?)(?:\s+out of\s+(\d+))?(?:\n|$)",
                                              original_text.replace("**", ""), re.IGNORECASE | re.DOTALL)

                    if BACK_WINS_MSG:
                        BB_COUNT = 00
                        try:
                            logging.info(BACK_WINS_MSG.group(1))
                            if BACK_WINS_MSG.group(1):
                                BB_COUNT = BACK_WINS_MSG.group(1)
                                BB_COUNT = f"{int(BB_COUNT):02d}"
                        except:
                            logging.exception("An error exception was thrown!")
                        modified_text = BACK_TO_BACK.format(str(BB_COUNT))
                        ent_m = BACK_TO_BACK_ENT
                    modified_text = await clean_text(modified_text)
                    sent = await client.send_message(
                        target_channel_id,
                        modified_text,
                        formatting_entities=ent_m,
                        link_preview=False
                    )
                    message_map[(event.chat_id, event.id)] = sent.id
                logging.info("Relayed message during session.")

        except Exception as e:
            logging.exception("An error exception was thrown!")

    session_status = "ACTIVE" if session_active else "CLOSED"
    logging.info("SESSION STATUS: {}".format(session_status))
    logging.info("🚀 Bot is running and waiting for messages TRADING KING VIP MAIN...")
    await client.run_until_disconnected()  # ⬅️ KEEP LISTENING


def start_telethon_king_vip():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(telethon_main())
