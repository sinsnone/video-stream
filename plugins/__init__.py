__version__ = "0.6.5"
# >>> patch : F.11.22

import time
import logging
from mody.yad import Bot

logging.basicConfig(
  filename=f'streambot-logs-{Bot.me.id}.txt',
  level=logging.INFO,
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("yt_dlp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("PyTgCalls").setLevel(logging.ERROR)

LOGS = logging.getLogger(__name__)
