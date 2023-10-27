#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20213849
API_HASH = "e97df0eca2a9531c80202c1a7d3f5721"
BOT_TOKEN = "6666983690:AAE09spYtWpC-E68x2LL4wfafdrzexlEGNs"
SESSION = "AQA438hHs69-8pMbEkN3ePR8xRFu_t5Gdnvsc8qWMFIwklrgs3slxd3NEkNx9NxY27p0qtC1eODl1ezS8vo_Ijzvt54acfUNxsKIVai4Zb5tGoEr2MqnxFxxIZZIJr_BtbpXYfUivBEaXKIEjakD01ixcMpaAw6JT4qEeov8xVv35kbEIikkJAnbGzvJJjv-PKEXOOP2b1rP2aIGBJazsQWzDq5vTsKVCLf6YtJnIUXQp51gdEHZXpBp9NA1hepSvidUaLxyHcZv8oEYy0BihKZnDDrAtfcfvBTWtz_aMcAxZ6xCGaIQoV0nI8xdaaC7AhaGB8SS2QC-q1cjj9vOUnvkAAAAAWDlE2QA"
FORCESUB = "Dizifilmarsivi"
AUTH = 5920592740

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
