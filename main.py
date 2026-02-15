import json
import logging
import os
import threading
import time
from datetime import datetime, time as dtime
import pytz
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from tradingking import app as king_vip_app, start_telethon_king_vip

load_dotenv()
MAIN_SESSION = os.environ['MAIN_SESSION']
tz = pytz.timezone("Asia/Karachi")

app = FastAPI()

telethon_started = {"king_vip": False}


def active_mode():
    now = datetime.now(tz).time()

    return MAIN_SESSION


def monitor_bots():
    while True:
        mode = active_mode()

        if mode == "king_vip" and not telethon_started['king_vip']:
            threading.Thread(target=start_telethon_king_vip, daemon=True).start()
            telethon_started["king_vip"] = True
            logging.info("king_vip bot started")

        time.sleep(30)


@app.on_event("startup")
def startup():
    threading.Thread(target=monitor_bots, daemon=True).start()


@app.get("/")
def root():
    mode = active_mode()
    return {"active": mode}


@app.api_route("/health", methods=["GET", "HEAD", "POST", "PUT"])
async def health_check():
    return {"status": "OK"}


# Mount both apps (routes exist but logic controls behavior)
app.mount("/king_vip", king_vip_app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
