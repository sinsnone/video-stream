from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME


bot = Client(
    ":veez:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="program")
)

user = Client(
    'SESSION_NAME',
    session_string=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

calls = PyTgCalls(user)

me_user = user.get_me()

with Client(":veez:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()