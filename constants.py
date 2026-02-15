from telegram import MessageEntity
from telethon.tl.types import MessageEntityBold, MessageEntityCustomEmoji, MessageEntityMention, MessageEntityUnderline

SIGNAL_DOWN = '''😎🔤🔤🔤🔤🔤🚨

🪙 {}
⏱   1 MINUTE
⏱  TRADE TIME  ▶️ {}

⭐️      TRADE DIRECTION      ⭐️

                 🔽DOWN🔽

🧠 TRADE WITH MARGIN ALWAYS ✅ 990001% SURESHOT TRADE ⚡️ @QuotexProfitKing✅'''

SIGNAL_UP = '''😎🔤🔤🔤🔤🔤🚨

🪙 {}
⏱   1 MINUTE
⏱  TRADE TIME  ▶️ {}

⭐️      TRADE DIRECTION      ⭐️

                 🔼UP 🔼

🧠 TRADE WITH MARGIN ALWAYS ✅ 990001% SURESHOT TRADE ⚡️ @QuotexProfitKing✅'''

SURESHOT_MSG = '''💰🧲99000001% SURESHOT 
PROFITKING BACK TO BACK WIN SURESHOT ✅

❤️ ITS DEEEP HYPER SURESHOT💘'''

WIN_MSG = '''⭐️      TRADE RESULT      ⭐️

          💰🏆 WIN 🏆💰'''

LOSS_MSG = '''⭐️      TRADE RESULT      ⭐️

             ⚠️  LOSS  ⚠️

KOI BAAT NAHI YE EAK TRADE GYA NO ISSUE 0️⃣ 
NEXT TRADE SURESHOT WIN 🎯  ➡️ MINDSET BUILD 🧠'''

ENT_OTC_UP: list[MessageEntity] = [
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
    MessageEntityBold(offset=18, length=12),
    MessageEntityBold(offset=30, length=1),
    MessageEntityCustomEmoji(offset=30, length=1, document_id=5458640241915084025),
    MessageEntityBold(offset=31, length=12),
    MessageEntityBold(offset=43, length=1),
    MessageEntityCustomEmoji(offset=43, length=1, document_id=5382194935057372936),
    MessageEntityBold(offset=44, length=14),
    MessageEntityBold(offset=58, length=2),
    MessageEntityCustomEmoji(offset=58, length=2, document_id=6266829404849050968),
    MessageEntityBold(offset=60, length=11),
    MessageEntityBold(offset=71, length=2),
    MessageEntityCustomEmoji(offset=71, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=73, length=27),
    MessageEntityBold(offset=100, length=2),
    MessageEntityCustomEmoji(offset=100, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=102, length=19),
    MessageEntityBold(offset=121, length=2),
    MessageEntityCustomEmoji(offset=121, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=123, length=3),
    MessageEntityBold(offset=126, length=2),
    MessageEntityCustomEmoji(offset=126, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=128, length=2),
    MessageEntityBold(offset=130, length=2),
    MessageEntityCustomEmoji(offset=130, length=2, document_id=5371053287380361807),
    MessageEntityBold(offset=132, length=26),
    MessageEntityBold(offset=158, length=1),
    MessageEntityCustomEmoji(offset=158, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=159, length=24),
    MessageEntityBold(offset=183, length=2),
    MessageEntityCustomEmoji(offset=183, length=2, document_id=5345905193005371012),
    MessageEntityBold(offset=185, length=1),
    MessageEntityMention(offset=186, length=17),
    MessageEntityBold(offset=186, length=17),
    MessageEntityBold(offset=203, length=1),
    MessageEntityCustomEmoji(offset=203, length=1, document_id=4985790168263820344),
]

ENT_OTC_DOWN: list[MessageEntity] = [
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
    MessageEntityBold(offset=18, length=12),
    MessageEntityBold(offset=30, length=1),
    MessageEntityCustomEmoji(offset=30, length=1, document_id=5458640241915084025),
    MessageEntityBold(offset=31, length=12),
    MessageEntityBold(offset=43, length=1),
    MessageEntityCustomEmoji(offset=43, length=1, document_id=5382194935057372936),
    MessageEntityBold(offset=44, length=14),
    MessageEntityBold(offset=58, length=2),
    MessageEntityCustomEmoji(offset=58, length=2, document_id=6266829404849050968),
    MessageEntityBold(offset=60, length=11),
    MessageEntityBold(offset=71, length=2),
    MessageEntityCustomEmoji(offset=71, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=73, length=27),
    MessageEntityBold(offset=100, length=2),
    MessageEntityCustomEmoji(offset=100, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=102, length=19),
    MessageEntityBold(offset=121, length=2),
    MessageEntityCustomEmoji(offset=121, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=123, length=4),
    MessageEntityBold(offset=127, length=2),
    MessageEntityCustomEmoji(offset=127, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=129, length=2),
    MessageEntityBold(offset=131, length=2),
    MessageEntityCustomEmoji(offset=131, length=2, document_id=5371053287380361807),
    MessageEntityBold(offset=133, length=26),
    MessageEntityBold(offset=159, length=1),
    MessageEntityCustomEmoji(offset=159, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=160, length=24),
    MessageEntityBold(offset=184, length=2),
    MessageEntityCustomEmoji(offset=184, length=2, document_id=5345905193005371012),
    MessageEntityBold(offset=186, length=1),
    MessageEntityMention(offset=187, length=17),
    MessageEntityBold(offset=187, length=17),
    MessageEntityBold(offset=204, length=1),
    MessageEntityCustomEmoji(offset=204, length=1, document_id=4985790168263820344),
]

ENT_LIVE_UP: list[MessageEntity] = [
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
    MessageEntityBold(offset=61, length=11),
    MessageEntityBold(offset=72, length=2),
    MessageEntityCustomEmoji(offset=72, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=74, length=27),
    MessageEntityBold(offset=101, length=2),
    MessageEntityCustomEmoji(offset=101, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=103, length=19),
    MessageEntityBold(offset=122, length=2),
    MessageEntityCustomEmoji(offset=122, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=124, length=3),
    MessageEntityBold(offset=127, length=2),
    MessageEntityCustomEmoji(offset=127, length=2, document_id=5449683594425410231),
    MessageEntityBold(offset=129, length=2),
    MessageEntityBold(offset=131, length=2),
    MessageEntityCustomEmoji(offset=131, length=2, document_id=5371053287380361807),
    MessageEntityBold(offset=133, length=26),
    MessageEntityBold(offset=159, length=1),
    MessageEntityCustomEmoji(offset=159, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=160, length=24),
    MessageEntityBold(offset=184, length=2),
    MessageEntityCustomEmoji(offset=184, length=2, document_id=5345905193005371012),
    MessageEntityBold(offset=186, length=1),
    MessageEntityMention(offset=187, length=17),
    MessageEntityBold(offset=187, length=17),
    MessageEntityBold(offset=204, length=1),
    MessageEntityCustomEmoji(offset=204, length=1, document_id=4985790168263820344),
]

ENT_LIVE_DOWN: list[MessageEntity] = [
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
    MessageEntityBold(offset=61, length=11),
    MessageEntityBold(offset=72, length=2),
    MessageEntityCustomEmoji(offset=72, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=74, length=27),
    MessageEntityBold(offset=101, length=2),
    MessageEntityCustomEmoji(offset=101, length=2, document_id=5274026806477857971),
    MessageEntityBold(offset=103, length=19),
    MessageEntityBold(offset=122, length=2),
    MessageEntityCustomEmoji(offset=122, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=124, length=4),
    MessageEntityBold(offset=128, length=2),
    MessageEntityCustomEmoji(offset=128, length=2, document_id=5447183459602669338),
    MessageEntityBold(offset=130, length=2),
    MessageEntityBold(offset=132, length=2),
    MessageEntityCustomEmoji(offset=132, length=2, document_id=5371053287380361807),
    MessageEntityBold(offset=134, length=26),
    MessageEntityBold(offset=160, length=1),
    MessageEntityCustomEmoji(offset=160, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=161, length=24),
    MessageEntityBold(offset=185, length=2),
    MessageEntityCustomEmoji(offset=185, length=2, document_id=5345905193005371012),
    MessageEntityBold(offset=187, length=1),
    MessageEntityMention(offset=188, length=17),
    MessageEntityBold(offset=188, length=17),
    MessageEntityBold(offset=205, length=1),
    MessageEntityCustomEmoji(offset=205, length=1, document_id=4985790168263820344),
]

SURESHOT_ENT: list[MessageEntity] = [
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5224257782013769471),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=4, length=57),
    MessageEntityBold(offset=61, length=1),
    MessageEntityCustomEmoji(offset=61, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=62, length=2),
    MessageEntityBold(offset=64, length=2),
    MessageEntityCustomEmoji(offset=64, length=2, document_id=5406926593698312391),
    MessageEntityBold(offset=66, length=25),
    MessageEntityBold(offset=91, length=2),
    MessageEntityCustomEmoji(offset=91, length=2, document_id=6282939930255563041),
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

BEFORE_TRADE = '''⚠️MUST Read THIS Before Trade! ⚠️

🚨 Follow These Simple Rules to Maximize Accuracy:

✅ Har trade mein sirf 1%–3% capital invest karein — strong risk management hi survival ki key hai.
✅1-Minute chart use karein aur trade expiry bhi 1 minute rakhein.
✅ Trade place karte waqt Time Mode select ho, Timer Mode nahi.
✅ Apne trading platform UTC +05:30 time zone par set zaroor karein.

📈 When you receive a signal ("UP" or "DOWN") —
➡️ IMMEDIATELY action lo — ek second ka delay bhi nahi!

🔥 Latest updates aur results ke liye PINNED MESSAGE check karo! 📌'''

GR_TEXT = '''✅ Get Ready! Session Starts at {} for BUG VIP SURESHOT SESSION...!! 🌀

📈 Currently Analyzing The Market To Deliver A Sharp, High-Quality Sureshots🔥'''

PUBLIC_SESSION_GR = '''✅ Get Ready! PUBLIC Session Will Start SOON for BUG SURESHOT SESSION...!! 🌀

📈 Currently Analyzing The Market To Deliver A Sharp, High-Quality Sureshots🔥'''

SIGNAL_PAIR = '''😎🔤🔤🔤🔤🔤🚨

🪙{}
⏱   1 MINUTE

💰 MY RISK ▶️ 💲2%'''

SURESHOT = '''💰🧲99000001% SURESHOT 
PROFITKING GUARRANTEED WINNING TRADE ✅

❤️ ITS DEEEP HYPER SURESHOT💘'''

RESULT = '''📊 VIP SESSION REPORT 😄😍🚀
📅 Date: {}

🔥 TOTAL STATS:
🔰 Wins: {} 🏆
🔰 Losses: {} 🧐

⭐️PROFIT KING ALWAYS ON TOP!! 99001% PROFIT 💵
99001% ACCURATE  💪'''

FEEDBACK_MSG = '''👑WAITING FOR YOUR REACTIONS & RESULTS 👑

   📱 Guys share you results: @QuotexProfitKing✅

 🔜 NEXT SIGNAL SOON 🔜'''

REACTIONS = '''👑DO REACTIONS IF YOUR ARE READY FOR SESSION KING FAMILY 👑

                                     🔜 SIGNAL SOON 🔜'''
WANT_MORE = '''🧲🧲 WANT 1 MORE DEEP SURESHOT??  👌👌
Guys us kaylye jaldi last trade keylye reactions aur feedbacks share kro 📣📣

🌟 PROFITKING ALWAYS ON TOP!! 🌟 

NO LOSS PERSONAL GUARANTEE HAI  ✅✅

 @QuotexProfitKing✅'''

BACK_TO_BACK = '''🔥🔥🧲🧲 BACK TO BACK DEEP {} SURESHOTS 🔥🔥🧲🧲

 🍾 POWER OF PROFITKING✅

💰🧲 QUOTEX MARKET CRACKED TODAY GUYS  💰🧲 

BAS VIP FAMILY 🌟 APNE APNE RESULTS SHARE KRO 📩
AUR REACTIONS SEND KRO JALDI!!  💧


📌⚡️ WANT 1 MORE DEEP SURESHOT??? ⚡️📌'''

BACK_TO_BACK_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5402406965252989103),
    MessageEntityBold(offset=2, length=2),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5424972470023104089),
    MessageEntityBold(offset=4, length=2),
    MessageEntityCustomEmoji(offset=4, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=6, length=2),
    MessageEntityCustomEmoji(offset=6, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=9, length=17),
    MessageEntityBold(offset=27, length=12),
    MessageEntityBold(offset=40, length=2),
    MessageEntityCustomEmoji(offset=40, length=2, document_id=5402406965252989103),
    MessageEntityBold(offset=42, length=2),
    MessageEntityCustomEmoji(offset=42, length=2, document_id=5424972470023104089),
    MessageEntityBold(offset=44, length=2),
    MessageEntityCustomEmoji(offset=44, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=46, length=2),
    MessageEntityCustomEmoji(offset=46, length=2, document_id=5202106638508512484),
    MessageEntityCustomEmoji(offset=51, length=2, document_id=5451814216031809603),
    MessageEntityBold(offset=54, length=19),
    MessageEntityCustomEmoji(offset=73, length=1, document_id=4985790168263820344),
    MessageEntityCustomEmoji(offset=76, length=2, document_id=5224257782013769471),
    MessageEntityCustomEmoji(offset=78, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=81, length=32),
    MessageEntityCustomEmoji(offset=115, length=2, document_id=5224257782013769471),
    MessageEntityCustomEmoji(offset=117, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=126, length=10),
    MessageEntityCustomEmoji(offset=137, length=2, document_id=5429386532467254041),
    MessageEntityBold(offset=150, length=7),
    MessageEntityCustomEmoji(offset=168, length=2, document_id=5368554037320900698),
    MessageEntityBold(offset=175, length=9),
    MessageEntityCustomEmoji(offset=203, length=2, document_id=5371058888017715839),
    MessageEntityCustomEmoji(offset=208, length=2, document_id=5397782960512444700),
    MessageEntityCustomEmoji(offset=210, length=2, document_id=5345905193005371012),
    MessageEntityBold(offset=213, length=28),
    MessageEntityCustomEmoji(offset=242, length=2, document_id=5345905193005371012),
    MessageEntityCustomEmoji(offset=244, length=2, document_id=5397782960512444700)
]

WANT_MORE_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=2, length=2),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=4, length=30),
    MessageEntityBold(offset=34, length=2),
    MessageEntityCustomEmoji(offset=34, length=2, document_id=5287478236027040039),
    MessageEntityBold(offset=36, length=2),
    MessageEntityCustomEmoji(offset=36, length=2, document_id=5287478236027040039),
    MessageEntityBold(offset=38, length=73),
    MessageEntityCustomEmoji(offset=112, length=2, document_id=5197304993920616826),
    MessageEntityCustomEmoji(offset=114, length=2, document_id=5197304993920616826),
    MessageEntityBold(offset=116, length=2),
    MessageEntityBold(offset=118, length=2),
    MessageEntityCustomEmoji(offset=118, length=2, document_id=5429386532467254041),
    MessageEntityBold(offset=121, length=26),
    MessageEntityCustomEmoji(offset=148, length=2, document_id=5429386532467254041),
    MessageEntityBold(offset=150, length=1),
    MessageEntityBold(offset=153, length=31),
    MessageEntityCustomEmoji(offset=185, length=1, document_id=5199628545457923796),
    MessageEntityCustomEmoji(offset=186, length=1, document_id=5199628545457923796),
    MessageEntityBold(offset=187, length=3),
    MessageEntityMention(offset=190, length=17),
    MessageEntityBold(offset=190, length=17),
    MessageEntityBold(offset=207, length=1),
    MessageEntityCustomEmoji(offset=207, length=1, document_id=4985790168263820344)
]

REACTIONS_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5431367272599920437),
    MessageEntityBold(offset=2, length=55),
    MessageEntityBold(offset=57, length=2),
    MessageEntityCustomEmoji(offset=57, length=2, document_id=5431367272599920437),
    MessageEntityBold(offset=59, length=39),
    MessageEntityBold(offset=98, length=2),
    MessageEntityCustomEmoji(offset=98, length=2, document_id=5440621591387980068),
    MessageEntityBold(offset=100, length=13),
    MessageEntityBold(offset=113, length=2),
    MessageEntityCustomEmoji(offset=113, length=2, document_id=5440621591387980068)
]

BT_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5420323339723881652),
    MessageEntityBold(offset=2, length=29),
    MessageEntityUnderline(offset=2, length=28),
    MessageEntityBold(offset=31, length=2),
    MessageEntityCustomEmoji(offset=31, length=2, document_id=5420323339723881652),
    MessageEntityBold(offset=33, length=2),
    MessageEntityBold(offset=35, length=2),
    MessageEntityCustomEmoji(offset=35, length=2, document_id=5395695537687123235),
    MessageEntityBold(offset=37, length=50),
    MessageEntityBold(offset=87, length=1),
    MessageEntityCustomEmoji(offset=87, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=88, length=97),
    MessageEntityBold(offset=186, length=1),
    MessageEntityCustomEmoji(offset=186, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=187, length=65),
    MessageEntityBold(offset=252, length=1),
    MessageEntityCustomEmoji(offset=252, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=253, length=62),
    MessageEntityBold(offset=315, length=1),
    MessageEntityCustomEmoji(offset=315, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=316, length=68),
    MessageEntityBold(offset=384, length=2),
    MessageEntityCustomEmoji(offset=384, length=2, document_id=5296644267467357718),
    MessageEntityBold(offset=386, length=46),
    MessageEntityBold(offset=432, length=2),
    MessageEntityCustomEmoji(offset=432, length=2, document_id=5433680387366728122),
    MessageEntityBold(offset=434, length=55),
    MessageEntityBold(offset=489, length=2),
    MessageEntityCustomEmoji(offset=489, length=2, document_id=5224344475928640252),
    MessageEntityBold(offset=491, length=63),
    MessageEntityBold(offset=554, length=2),
    MessageEntityCustomEmoji(offset=554, length=2, document_id=5397782960512444700)
]

GR_ENT: list[MessageEntity] = [
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5895553744380103925),
    MessageEntityBold(offset=2, length=54),
    MessageEntityCustomEmoji(offset=56, length=2, document_id=5372917041193828849),
    MessageEntityCustomEmoji(offset=60, length=2, document_id=5388584922975857751),
    MessageEntityBold(offset=62, length=71),
    MessageEntityBold(offset=134, length=19),
    MessageEntityBold(offset=153, length=2),
    MessageEntityCustomEmoji(offset=153, length=2, document_id=6267032805910254913),
    MessageEntityBold(offset=0, length=1),
    MessageEntityCustomEmoji(offset=0, length=1, document_id=5213287958798410406),
    MessageEntityBold(offset=2, length=37),
    MessageEntityBold(offset=40, length=33),
    MessageEntityCustomEmoji(offset=74, length=2, document_id=5370715282044100355),
    MessageEntityBold(offset=76, length=2),
    MessageEntityBold(offset=78, length=2),
    MessageEntityCustomEmoji(offset=78, length=2, document_id=5244837092042750681),
    MessageEntityBold(offset=80, length=74),
    MessageEntityBold(offset=154, length=2),
    MessageEntityCustomEmoji(offset=154, length=2, document_id=5463154755054349837)
]

SIGNAL_PAIR_ENT: list[MessageEntity] = [
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
    MessageEntityBold(offset=18, length=7),
    MessageEntityBold(offset=26, length=4),
    MessageEntityBold(offset=30, length=1),
    MessageEntityCustomEmoji(offset=30, length=1, document_id=5458640241915084025),
    MessageEntityBold(offset=31, length=13),
    MessageEntityBold(offset=44, length=2),
    MessageEntityCustomEmoji(offset=44, length=2, document_id=6066411529144638745),
    MessageEntityBold(offset=46, length=9),
    MessageEntityBold(offset=55, length=2),
    MessageEntityCustomEmoji(offset=55, length=2, document_id=6266829404849050968),
    MessageEntityBold(offset=57, length=1),
    MessageEntityBold(offset=58, length=2),
    MessageEntityCustomEmoji(offset=58, length=2, document_id=5390875094027344872),
    MessageEntityBold(offset=60, length=2)
]

SURESHOT_ENT: list[MessageEntity] = [
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5224257782013769471),
    MessageEntityCustomEmoji(offset=2, length=2, document_id=5202106638508512484),
    MessageEntityBold(offset=4, length=57),
    MessageEntityBold(offset=61, length=1),
    MessageEntityCustomEmoji(offset=61, length=1, document_id=5260463209562776385),
    MessageEntityBold(offset=62, length=2),
    MessageEntityBold(offset=64, length=2),
    MessageEntityCustomEmoji(offset=64, length=2, document_id=5406926593698312391),
    MessageEntityBold(offset=66, length=25),
    MessageEntityBold(offset=91, length=2),
    MessageEntityCustomEmoji(offset=91, length=2, document_id=6282939930255563041)
]

RESULT_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5231200819986047254),
    MessageEntityBold(offset=2, length=20),
    MessageEntityBold(offset=22, length=2),
    MessageEntityCustomEmoji(offset=22, length=2, document_id=6217630318250168874),
    MessageEntityBold(offset=24, length=2),
    MessageEntityCustomEmoji(offset=24, length=2, document_id=6217523115866459467),
    MessageEntityBold(offset=26, length=2),
    MessageEntityCustomEmoji(offset=26, length=2, document_id=6068700050928704109),
    MessageEntityBold(offset=28, length=1),
    MessageEntityBold(offset=29, length=2),
    MessageEntityCustomEmoji(offset=29, length=2, document_id=5472279086657199080),
    MessageEntityBold(offset=31, length=20),
    MessageEntityBold(offset=51, length=2),
    MessageEntityCustomEmoji(offset=51, length=2, document_id=5389038097860144794),
    MessageEntityBold(offset=53, length=26),
    MessageEntityBold(offset=79, length=2),
    MessageEntityCustomEmoji(offset=79, length=2, document_id=5188344996356448758),
    MessageEntityBold(offset=81, length=14),
    MessageEntityBold(offset=96, length=2),
    MessageEntityCustomEmoji(offset=96, length=2, document_id=5402461597237004802),
    MessageEntityBold(offset=98, length=2),
    MessageEntityBold(offset=100, length=2),
    MessageEntityCustomEmoji(offset=100, length=2, document_id=5370784581341422520),
    MessageEntityBold(offset=102, length=42),
    MessageEntityBold(offset=144, length=2),
    MessageEntityCustomEmoji(offset=144, length=2, document_id=5409048419211682843),
    MessageEntityBold(offset=146, length=17),
    MessageEntityCustomEmoji(offset=164, length=2, document_id=5463413771647069835)
]

FEEDBACK_MSG_ENT: list[MessageEntity] = [
    MessageEntityBold(offset=0, length=2),
    MessageEntityCustomEmoji(offset=0, length=2, document_id=5431367272599920437),
    MessageEntityBold(offset=2, length=36),
    MessageEntityCustomEmoji(offset=39, length=2, document_id=5431367272599920437),
    MessageEntityBold(offset=42, length=1),
    MessageEntityCustomEmoji(offset=46, length=2, document_id=5220069871072583573),
    MessageEntityBold(offset=49, length=24),
    MessageEntityMention(offset=73, length=17),
    MessageEntityBold(offset=73, length=17),
    MessageEntityBold(offset=90, length=1),
    MessageEntityCustomEmoji(offset=90, length=1, document_id=4985790168263820344),
    MessageEntityBold(offset=91, length=3),
    MessageEntityBold(offset=94, length=2),
    MessageEntityCustomEmoji(offset=94, length=2, document_id=5440621591387980068),
    MessageEntityBold(offset=96, length=18),
    MessageEntityBold(offset=114, length=2),
    MessageEntityCustomEmoji(offset=114, length=2, document_id=5440621591387980068)
]

