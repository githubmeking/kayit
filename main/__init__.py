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
SESSION = "AQCnPNrkeL-ow9RAl21VKo3UtnLycHgIsQoiP5tQskt3O_hFLQWeBsHVLHA7WnmreLbzmck-NkS8M6pBj_w1O3AmPLfXofYFWp7o_eLY1vzKzxOAswmNThjkO9CFK13dqRPrcpkxZLONTbys3APP56yuYVzbrXS_UIUJjJjAvZ6XqUcdwteKtIpgtaH_td8TxLEs-jZtm8Mc8xOtrydHjIu_uXHy01jxMjr1yfJBs18fHvMG33KRB_QylXK14vQZhAksIyOPwK2gQdaussiIJ03nDPN84-XN_0bmmVHTFe3nBR_RsZobH1hm_mp-YMscdwZmqOcIagZ-jZdKNpmB30EDAAAAAWDlE2QA"
FORCESUB = "Dizifilmarsivi"
AUTH = 5920592740

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
