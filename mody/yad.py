from pyrogram import Client
from pyrogram import filters
from pytgcalls import PyTgCalls
from pyrolistener import Listener
from mody.Redis import db
from mody.get_info import token, sudo_info, get_bot
from info import session

Bot = Client(
    'MainBot',
    27786450,
    '1fb7b1af2837205d7ce8d77cefc0acbd',
    bot_token=token,
    plugins=dict(root='plugins')
)

user = Client(
    "MainUser",
    27786450,
    '1fb7b1af2837205d7ce8d77cefc0acbd',
    session_string=session
)

calls = PyTgCalls(user)

def Bfilter(text):
    return filters.msg(text) & filters.private & filters.user(sudo_info.id)

listener = Listener(client=Bot, show_output=True)