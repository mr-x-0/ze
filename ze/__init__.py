import logging
import time
import sys
import ze.core.ubclient
from .config import Var
from .core.client import ZeClient
from .core.session import both_session
from .core.logger import *
from database import zedB, zedB

version = "1.0.0"
start_time = time.time()
bot_token = zedB.get_config("BOT_TOKEN")


zeubot = ze_bot = ZeClient(
        session=both_session(Var.SESSION, LOGS),
        app_version=version,
        device_model="Ze",
       )


tgbot = asst = ZeClient("Tgbot", bot_token=bot_token)

del bot_token


HNDLR = zedB.get_key("HNDLR") or "."
SUDO_HNDLR = zedB.get_key("SUDO_HNDLR") or HNDLR
