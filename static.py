import os

from dotenv import load_dotenv
from telegram import MessageEntity
from telethon.tl.types import MessageEntityBold, MessageEntityMention, MessageEntityCustomEmoji, MessageEntityTextUrl

load_dotenv(),
REF_URL = os.environ['REF_URL']

CALL_TRADE_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5422565505925928085),
    MessageEntityBold(offset=2, length=2),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5384082895306499733),
    MessageEntityBold(offset=4, length=2),
    MessageEntityCustomEmoji(offset=4, length=2, document_id=5384455741417466563),
    MessageEntityBold(offset=6, length=2),
    MessageEntityCustomEmoji(offset=6, length=2, document_id=5382232065049635651),
    MessageEntityBold(offset=8, length=2),
    MessageEntityCustomEmoji(offset=8, length=2, document_id=5381823532055405217),
    MessageEntityBold(offset=10, length=2),
    MessageEntityCustomEmoji(offset=10, length=2, document_id=5381872065185850245),
    MessageEntityBold(offset=12, length=2),
    MessageEntityCustomEmoji(offset=12, length=2, document_id=5260750418320836046),
    MessageEntityBold(offset=14, length=2),
    MessageEntityBold(offset=16, length=2),
    MessageEntityCustomEmoji(offset=16, length=2, document_id=5202064723922670546),
    MessageEntityBold(offset=18, length=13),
    MessageEntityBold(offset=31, length=1),
    MessageEntityCustomEmoji(offset=31, length=1, document_id=5458640241915084025),
    MessageEntityBold(offset=32, length=12),
    MessageEntityBold(offset=44, length=1),
    MessageEntityCustomEmoji(offset=44, length=1, document_id=5382194935057372936),
    MessageEntityBold(offset=45, length=14),
    MessageEntityBold(offset=59, length=2),
    MessageEntityCustomEmoji(offset=59, length=2, document_id=6266829404849050968),
    MessageEntityBold(offset=61, length=17),
    MessageEntityBold(offset=78, length=2),
    MessageEntityCustomEmoji(offset=78, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=80, length=4),
    MessageEntityBold(offset=84, length=2),
    MessageEntityCustomEmoji(offset=84, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=86, length=2),
    MessageEntityMention(offset=88, length=17),
    MessageEntityBold(offset=88, length=17),
    MessageEntityBold(offset=105, length=1),
    MessageEntityCustomEmoji(offset=105, length=1, document_id=4985790168263820344),
    MessageEntityBold(offset=106, length=5),
    MessageEntityTextUrl(offset=111, length=21, url='https://market-qx.trade/sign-up?lid={}'.format(REF_URL)),
    MessageEntityBold(offset=111, length=21),
]

PUT_TRADE_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5422565505925928085),
    MessageEntityBold(offset=2, length=2),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5384082895306499733),
    MessageEntityBold(offset=4, length=2),
    MessageEntityCustomEmoji(offset=4, length=2, document_id=5384455741417466563),
    MessageEntityBold(offset=6, length=2),
    MessageEntityCustomEmoji(offset=6, length=2, document_id=5382232065049635651),
    MessageEntityBold(offset=8, length=2),
    MessageEntityCustomEmoji(offset=8, length=2, document_id=5381823532055405217),
    MessageEntityBold(offset=10, length=2),
    MessageEntityCustomEmoji(offset=10, length=2, document_id=5381872065185850245),
    MessageEntityBold(offset=12, length=2),
    MessageEntityCustomEmoji(offset=12, length=2, document_id=5260750418320836046),
    MessageEntityBold(offset=14, length=2),
    MessageEntityBold(offset=16, length=2),
    MessageEntityCustomEmoji(offset=16, length=2, document_id=5202064723922670546),
    MessageEntityBold(offset=18, length=13),
    MessageEntityBold(offset=31, length=1),
    MessageEntityCustomEmoji(offset=31, length=1, document_id=5458640241915084025),
    MessageEntityBold(offset=32, length=12),
    MessageEntityBold(offset=44, length=1),
    MessageEntityCustomEmoji(offset=44, length=1, document_id=5382194935057372936),
    MessageEntityBold(offset=45, length=14),
    MessageEntityBold(offset=59, length=2),
    MessageEntityCustomEmoji(offset=59, length=2, document_id=6266829404849050968),
    MessageEntityBold(offset=61, length=17),
    MessageEntityBold(offset=78, length=2),
    MessageEntityCustomEmoji(offset=78, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=80, length=4),
    MessageEntityBold(offset=84, length=2),
    MessageEntityCustomEmoji(offset=84, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=86, length=2),
    MessageEntityMention(offset=88, length=17),
    MessageEntityBold(offset=88, length=17),
    MessageEntityBold(offset=105, length=1),
    MessageEntityCustomEmoji(offset=105, length=1, document_id=4985790168263820344),
    MessageEntityBold(offset=106, length=5),
    MessageEntityTextUrl(offset=111, length=21, url='https://market-qx.trade/sign-up?lid={}'.format(REF_URL)),
    MessageEntityBold(offset=111, length=21),
]


WIN_MSG_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=2, length=24),
    MessageEntityBold(offset=26, length=2),
    MessageEntityCustomEmoji(offset=26, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=28, length=12),
    MessageEntityBold(offset=40, length=2),
    MessageEntityCustomEmoji(offset=40, length=2, document_id=5224257782013769471),
    MessageEntityBold(offset=42, length=2),
    MessageEntityCustomEmoji(offset=42, length=2, document_id=5188344996356448758),
    MessageEntityBold(offset=44, length=5),
    MessageEntityBold(offset=49, length=2),
    MessageEntityCustomEmoji(offset=49, length=2, document_id=5188344996356448758),
    MessageEntityBold(offset=51, length=2),
    MessageEntityCustomEmoji(offset=51, length=2, document_id=5224257782013769471),
]

LOSS_MSG_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=2, length=24),
    MessageEntityBold(offset=26, length=2),
    MessageEntityCustomEmoji(offset=26, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=28, length=15),
    MessageEntityBold(offset=43, length=2),
    MessageEntityCustomEmoji(offset=43, length=2, document_id=5420323339723881652),
    MessageEntityBold(offset=45, length=8),
    MessageEntityBold(offset=53, length=2),
    MessageEntityCustomEmoji(offset=53, length=2, document_id=5420323339723881652),
    MessageEntityBold(offset=55, length=42),
    MessageEntityBold(offset=97, length=3),
    MessageEntityCustomEmoji(offset=97, length=3, document_id=5217809408309861154),
    MessageEntityBold(offset=100, length=26),
    MessageEntityBold(offset=126, length=2),
    MessageEntityCustomEmoji(offset=126, length=2, document_id=5310278924616356636),
    MessageEntityBold(offset=128, length=2),
    MessageEntityBold(offset=130, length=2),
    MessageEntityCustomEmoji(offset=130, length=2, document_id=5416117059207572332),
    MessageEntityBold(offset=132, length=14),
    MessageEntityCustomEmoji(offset=147, length=2, document_id=5371053287380361807),
]

MTG_WIN_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=2, length=24),
    MessageEntityBold(offset=26, length=2),
    MessageEntityCustomEmoji(offset=26, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=28, length=6),
    MessageEntityBold(offset=34, length=2),
    MessageEntityCustomEmoji(offset=34, length=2, document_id=5224257782013769471),
    MessageEntityBold(offset=36, length=2),
    MessageEntityCustomEmoji(offset=36, length=2, document_id=5188344996356448758),
    MessageEntityBold(offset=38, length=9),
    MessageEntityBold(offset=47, length=2),
    MessageEntityCustomEmoji(offset=47, length=2, document_id=5188344996356448758),
    MessageEntityBold(offset=49, length=2),
    MessageEntityCustomEmoji(offset=49, length=2, document_id=5224257782013769471)
]

WIN_MSG = '''⭐️      TRADE RESULT      ⭐️

          💰🏆 WIN 🏆💰'''

LOSS_MSG = '''⭐️      TRADE RESULT      ⭐️

             ⚠️  LOSS  ⚠️

KOI BAAT NAHI YE EAK TRADE GYA NO ISSUE 0️⃣ 
NEXT TRADE SURESHOT WIN 🎯  ➡️ MINDSET BUILD 🧠'''

MTG_WIN = '''⭐️      TRADE RESULT      ⭐️

    💰🏆 MTG WIN 🏆💰'''

PUT_TRADE = '''😎🔤🔤🔤🔤🔤🚨

🪙 {}
⏱   1 MINUTE
⏱  TRADE TIME  ▶️ {}

         🔽DOWN🔽

@QuotexProfitKing✅     CREATE QUOTEX ACCOUNT'''

CALL_TRADE = '''😎🔤🔤🔤🔤🔤🚨

🪙 {}
⏱   1 MINUTE
⏱  TRADE TIME  ▶️ {}

         🔼 UP 🔼

@QuotexProfitKing✅     CREATE QUOTEX ACCOUNT'''