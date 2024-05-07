import logging
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pyromod import listen

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

calls = PyTgCalls(user)

# Configure the logger
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

async def start_bot():
    await bot.start()
    try:
        await user.start()
    except Exception as e:
        logger.exception(e)
    print("تم تشغيل البوت بنجاح")
    await idle()
    await bot.stop()
    print("تم ايقاف البوت بنجاح")

with Client(":veez:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
    
with user as app:
    me_user = app.get_me()