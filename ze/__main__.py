from . import *

import contextlib
import os
import sys
import time
from .core.helper import time_formatter#, bash
from .load_plug import load
from telethon.errors import SessionRevokedError
from .utils import (
    join_dev,
    main_process,
)


zeubot.me.phone = None

if not zeubot.me.bot:
    zedB.set_key("OWNER_ID", zeubot.me.id)
    zedB.set_key("NAME", zeubot.full_name)


LOGS.info("جار تثبيت سورس زد إي ...")


try:
    LOGS.info("يتم أعداد الأعدادات")
    zeubot.loop.run_until_complete(main_process())
    LOGS.info("تم اعداد اعدادت سورس زد إي ✅")
except Exception as meo:
    LOGS.error(f"- {meo}")
    sys.exit()

zeubot.loop.create_task(join_dev())

async def load_plugins():
    load(path=["plugins/basic", "plugins/assistant","plugins/account","plugins/fun","plugins/group"])

zeubot.run_in_loop(load_plugins())


LOGS.info(f"⏳ تم استغراق {time_formatter((time.time() - start_time) * 1000)} ميللي ثانية لبدء تشغيل سورس زد إي.")

LOGS.info(
    """
    ╔══════════════════════════════════════════╗
    ║       ✅ تم تنصيب وتشغيل سورس زد إي بنجاح             ║ 
    ║       تابع آخر التحديثات من خلال قناة @SOURCEZE            ║
    ╚══════════════════════════════════════════╝
    """
)

    
try:
    asst.run()
    LOGS.info(f"تم بنجاح تشغيل البوت المساعد من @SOURCEZE")
except SessionRevokedError:
    LOGS.info(f"جلسة البوت المساعد [@{asst.me.username}] فشلت لكن سيتم تشغيل سورس الحساب فقط")
    zeubot.run()

