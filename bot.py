import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URL, SESSION_NAME, BOT_USERNAME, DEV, LOGGER_ID, OWNER_NAME, appp, user as usr, helper as ass, call
from pyromod import listen
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from plugins.info import activecall, helper, active
from plugins.Data import db, dev, devname, set_must, get_data

bot = Client(
    "MainBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
    )

user = Client(
    "MainUser",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_NAME
)

# Configure the logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance
logger = logging.getLogger(__name__)
mongodb = _mongo_client_(MONGO_DB_URL)
mo = MongoClient()
mo = MongoClient(MONGO_DB_URL)
moo = mo["data"]
Bots = moo.njsa
db = mongodb.db
botdb = db.botdb
blockdb = db.blocked
Done = []
OFF = True

async def start_bot():
    data = {"bot_username": BOT_USERNAME, "token": BOT_TOKEN, "session": SESSION_NAME, "dev": DEV, "logger": LOGGER_ID, "logger_mode": "ON"}
    Bots.insert_one(data)
    activecall[BOT_USERNAME] = []
    dev[BOT_USERNAME] = DEV
    await bot.start()
    try:
        devo = await bot.get_chat(DEV)
        devo = devo.first_name
        devname[BOT_USERNAME] = devo
    except:
        devname[BOT_USERNAME] = OWNER_NAME
    try:
        await user.start()
    except Exception as e:
        logger.exception(e)
    appp[BOT_USERNAME] = bot
    usr[BOT_USERNAME] = user
    ass[BOT_USERNAME] = []
    await helper(BOT_USERNAME)
    print("تم تشغيل البوت بنجاح")
    await idle()
    await Bot.stop()
    print("تم ايقاف البوت بنجاح")
