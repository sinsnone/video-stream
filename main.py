import asyncio
from pyrogram import idle
from mody.Redis import db
from mody.get_info import sudo_info, get_bot
from mody.yad import Bot, user, calls

async def main():
    await Bot.start()
    try:
        await user.start()
    except:
        print("جلسه لا تعمل")
    try:
        await calls.start()
    except:
        print("جلسه لا تعمل")
    print("تم تشغيل البوت بنجاح")
    await idle()
    await Bot.stop()
    print("تم ايقاف البوت بنجاح")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())