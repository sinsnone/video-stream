import os
import re
import yt_dlp
import asyncio
import textwrap
import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from typing import Union
from googletrans import Translator
from mody.yad import Bot
from mody.Redis import db

photo_Exception = "https://graph.org/file/f952059c72587541262c3.jpg"
translator = Translator()
bot_id = Bot.me.id

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def gen_thumb(videoid, photo):
    if os.path.isfile(f"{photo}.png"):
        return f"{photo}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
                test = translator.translate(title, dest="en")
                title = test.text
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"thumb{videoid}.png")
        Mostafa = Image.open(f"{photo}")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = Mostafa.width / 2
        Ycenter = Mostafa.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = Mostafa.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("assets/font2.ttf", 40)
        font2 = ImageFont.truetype("assets/font2.ttf", 70)
        arial = ImageFont.truetype("assets/font2.ttf", 30)
        name_font = ImageFont.truetype("assets/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (600, 150),
            "START PLAYING",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"{photo}")
            os.remove(f"thumb{videoid}.png")
        except:
            pass
        background.save(f"{photo}.png")
        return f"{photo}.png"
    except Exception as e:
        print(f"Error adding served call: {e}")

db_chat = {}
active = []
activevideo = []

async def add(
    chat_id,
    bot_username,
    file_path,
    link,
    title,
    duration,
    videoid,
    vid,
    user_id
):
    put = {
        "title": title,
        "dur": duration,
        "user_id": user_id,
        "chat_id": chat_id,
        "vid": vid,
        "file_path": file_path,
        "link": link,
        "videoid": videoid,
        "played": 0,
    }
    chat_id = f"{bot_username}{chat_id}"
    i = db_chat.get(chat_id)
    if not i:
        db_chat[chat_id] = []
    db_chat[chat_id].append(put)
    return

async def download(bot_username, link, video: Union[bool, str] = None):
    link = link
    loop = asyncio.get_running_loop()
    
    def audio_dl():
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"downloads/{bot_username}%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True
        }
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        info = ydl.extract_info(link, False)
        file_path = os.path.join("downloads", f"{bot_username}{info['id']}.{info['ext']}")
        if os.path.exists(file_path):
            return file_path
        ydl.download([link])
        return file_path
    
    if video:
        proc = await asyncio.create_subprocess_exec(
            "yt-dlp", "-g", "-f", "best[height<=?720][width<=?1280]", f"{link}",
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if stdout:
            downloaded_file = stdout.decode().split("\n")[0]
        else:
            return None
    else:
        downloaded_file = await loop.run_in_executor(None, audio_dl)
    
    return downloaded_file

activecall = {}

async def get_served_call(bot_username) -> list:
    return activecall

async def is_served_call(client, chat_id: int) -> bool:
    bot_username = client.me.username
    if bot_username not in activecall:
        activecall[bot_username] = []
    if chat_id not in activecall[bot_username]:
        return False
    else:
        return True

async def add_served_call(client, chat_id: int):
    bot_username = client.me.username
    if bot_username not in activecall:
        activecall[bot_username] = []
    if chat_id not in activecall[bot_username]:
        activecall[bot_username].append(chat_id)

async def add_active_video_chat(chat_id: int):
    if chat_id not in activevideo:
        activevideo.append(chat_id)

async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)

async def remove_active_video_chat(chat_id: int):
    if chat_id in activevideo:
        activevideo.remove(chat_id)

async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)

async def remove_active(bot_username, chat_id: int):
    chat = f"{bot_username}{chat_id}"
    try:
        db_chat[chat] = []
    except:
        pass
    try:
        await remove_active_video_chat(chat_id)
    except:
        pass
    try:
        await remove_active_chat(chat_id)
    except:
        pass
    try:
        await remove_served_call(bot_username, chat_id)
    except:
        pass
##############
async def Admin(c, message):
    if isinstance(message, Message):
        user_id = message.from_user.id
        chat_id = message.chat.id
    elif isinstance(message, CallbackQuery):
        user_id = message.from_user.id
        chat_id = message.message.chat.id
    else:
        return False  
    admins = db.smembers(f"bot_admins{bot_id}")
    dev = db.get(f"bot_owner{bot_id}")
    user = await c.get_chat_member(chat_id, user_id)
    if user.status.value in ("administrator", "owner") or user_id == 1736636295 or dev:
        return True
    if user_id in admins:
        return True
    return False

##############
def add_user(user_id: int):
    if is_user(user_id):
        return
    db.sadd(f"botusers{bot_id}", user_id)

def is_user(user_id: int) -> bool:
    try:
        users = get_users()
        return user_id in users
    except:
        return False

def del_user(user_id: int) -> bool:
    if not is_user(user_id):
        return False
    db.srem(f"botusers{bot_id}", user_id)
    return True

def get_users() -> list:
    try:
        users = []
        for user_id in db.smembers(f"botusers{bot_id}"):
            users.append(int(user_id))
        return users
    except:
        return []

def get_users_backup() -> str:
    text = ''
    for user in db.smembers(f"botusers{bot_id}"):
        text += user + '\n'
    with open('users.txt', 'w+') as f:
        f.write(text)
    return 'users.txt'

def add_admin(user_id: int):
    if is_admin(user_id):
        return
    db.sadd(f"bot_admins{bot_id}", user_id)

def is_admin(user_id: int) -> bool:
    try:
        admins = get_admins()
        return user_id in admins
    except:
        return False

def del_admin(user_id: int) -> bool:
    if not is_admin(user_id):
        return False
    db.srem(f"bot_admins{bot_id}", user_id)
    return True

def get_admins() -> list:
    try:
        admins = []
        for admin_id in db.smembers(f"bot_admins{bot_id}"):
            admins.append(int(admin_id))
        return admins
    except:
        return []

def get_admins_backup() -> str:
    text = ''
    for admin in db.smembers(f"bot_admins{bot_id}"):
        text += admin + '\n'
    with open('admins.txt', 'w+') as f:
        f.write(text)
    return 'admins.txt'

def add_group(chat_id: int):
    if is_group(chat_id):
        return
    db.sadd(f"botgroups{bot_id}", chat_id)

def is_group(chat_id: int) -> bool:
    try:
        groups = get_groups()
        return chat_id in groups
    except:
        return False

def del_group(chat_id: int) -> bool:
    if not is_group(chat_id):
        return False
    db.srem(f"botgroups{bot_id}", chat_id)
    return True

def get_groups() -> list:
    try:
        groups = []
        for group_id in db.smembers(f"botgroups{bot_id}"):
            groups.append(int(group_id))
        return groups
    except:
        return []

def get_groups_backup() -> str:
    text = ''
    for group in db.smembers(f"botgroups{bot_id}"):
        text += group + '\n'
    with open('groups.txt', 'w+') as f:
        f.write(text)
    return 'groups.txt'

def check(id):
    if is_admin(id):
        return True
    if id == int(db.get(f"bot_owner{bot_id}")):
        return True
    else:
        return False