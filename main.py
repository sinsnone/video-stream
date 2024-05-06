import asyncio
import logging
from pyrogram import Client, idle
from program import LOGS
from driver.core import calls, bot, user
from config import API_HASH, API_ID, BOT_TOKEN

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


bot = Client(
    ":veez:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="program")
)

async def start_bot():
    await bot.start()
    try:
        await user.start()
        await calls.start()
        await user.join_chat("iwiwwiq")
        await user.join_chat("xxStitch")
    except Exception as e:
        logger.exception(e)
    print("تم تشغيل البوت بنجاح")
    await idle()
    await Bot.stop()
    print("تم ايقاف البوت بنجاح")

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(start_bot())
