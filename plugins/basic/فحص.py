"""
۞ `{i}فحص`
    لـ عرض حالة سورس زد إي والاصدار و وقت التشغيل

۞ ملاحظة: يمكنك وضع او تغيير الصورة من خلال البوت المساعد الخاص بك


۞ `{i}بنك`
    أمر تجريبي لتجربة السورس 

"""

import os
from platform import python_version
from random import choice
from datetime import datetime
from ze.config import version
from telethon.errors import BotMethodInvalidError, ChatSendMediaForbiddenError
from telethon.extensions import html, markdown
from telethon.utils import resolve_bot_file_id
from telethon.version import __version__
from .. import *


buttons = [
    [
        Button.url("مجموعة المساعدة", "t.me/ZESUPORT"),
        Button.url("قناة السورس", "t.me/SOURCEZE"),
    ]
]

alive_txt = """
سورس زد إي يعمل بنجاح

  ۞ أصدار زد إي - {}
  ۞ أصدار التليليثون - {}
"""

PING_PIC = ZedB.get_key("PING_PIC") or "https://files.catbox.moe/bk64x4.jpg"
ZE_TXT = "ابتسم فهناك شتاء قادم وصباحات ٌممطرةٌ . ."


in_alive = "{}\n\n۞ <b>إصدار زد إي -><b> <code>{}</code>\n۞ <b>إصدار البايثون -></b> <code>{}</code>\n۞ <b>مدة التشغيل -></b> <code>{}</code>\n\n<b>قناة السورس @SOURCEZE</b>"
alive_1 = "**سورس زد إي يعمل بنجاح ✅**\n\n۞ **مالك الحساب** - `{}`\n۞ **إصدار زد إي** - `{}`\n۞ **مدة التشغيل** - `{}`\n۞ **إصدار البايثون** - `{}`\n۞ **إصدار التيليثون** - `{}`\n@SOURCEZE"


@callback("alive")
async def alive(event):
    text = alive_txt.format(version, __version__)
    await event.answer(text, alert=True)


@ze_cmd(pattern="فحص( (.*)|$)")
async def alive_func(e):
    match = e.pattern_match.group(1).strip()
    inline = None
    if match in ["انلاين", "إنلاين"]:
        try:
            res = await e.client.inline_query(tgbot.me.username, "alive")
            return await res[0].click(e.chat_id)
        except BotMethodInvalidError:
            pass
        except BaseException as er:
            LOGS.exception(er)
        inline = True
    OWNER_NAME = zeubot.me.first_name

    pic = zedB.get_key("ALIVE_PIC") or "https://files.catbox.moe/bk64x4.jpg"
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    if inline:
        parse = html
        als = in_alive.format(
            version,
            python_version(),
            uptime
        )

        if _e := zedB.get_key("ALIVE_EMOJI"):
            als = als.replace("۞", _e)
    else:
        parse = markdown
        als = alive_1.format(
                OWNER_NAME,
                version,
                uptime,
                python_version(),
                __version__
                )

        if a := zedB.get_key("ALIVE_EMOJI"):
            als = als.replace("۞", a)
    if pic:
        try:
            await e.reply(
                als,
                file=pic,
                parse_mode=parse,
                link_preview=False,
                buttons=buttons if inline else None,
            )
            return await e.try_delete()
        except ChatSendMediaForbiddenError:
            pass
        except BaseException as er:
            LOGS.exception(er)
            try:
                await e.reply(file=pic)
                await e.reply(
                    als,
                    parse_mode=parse,
                    buttons=buttons if inline else None,
                    link_preview=False,
                )
                return await e.try_delete()
            except BaseException as er:
                LOGS.exception(er)
    await e.eor(
        als,
        parse_mode=parse,
        link_preview=False,
        buttons=buttons if inline else None,
    )


@in_pattern("alive", owner=True)
async def inline_alive(e):
    pic = zedB.get_key("ALIVE_PIC") or "https://files.catbox.moe/mkpve6.webp"
    if isinstance(pic, list):
        pic = choice(pic)
    uptime = time_formatter((time.time() - start_time) * 1000)
    als = in_alive.format(
        version, python_version(), uptime
    )

    if _e := zedB.get_key("ALIVE_EMOJI"):
        als = als.replace("۞", _e)
    builder = e.builder
    if pic:
        try:
            if ".jpg" in pic:
                results = [
                    await builder.photo(
                        pic, text=als, parse_mode="html", buttons=buttons
                    )
                ]
            else:
                if _pic := resolve_bot_file_id(pic):
                    pic = _pic
                    buttons.insert(
                        0, [Button.inline("Stats", data="alive")]
                    )
                results = [
                    await builder.document(
                        pic,
                        title="Inline Alive",
                        description="@SOURCEZE",
                        parse_mode="html",
                        buttons=buttons,
                    )
                ]
            return await e.answer(results)
        except BaseException as er:
            LOGS.exception(er)
    result = [
        await builder.article(
            "Alive", text=als, parse_mode="html", link_preview=False, buttons=buttons
        )
    ]
    await e.answer(result)


@ze_cmd(pattern="بنك$")
async def ping_cmd(event):
    start = datetime.now()
    ms = (datetime.now() - start).microseconds / 1000
    caption = f"<b><i>{ZE_TXT}<i><b>\n<code>┏━━━━━━━┓\n┃ ✦ {ms}\n┃ ✦ <b>{zeubot.me.first_name}</b>\n┗━━━━━━━┛"
    
    await event.client.send_file(
        event.chat_id,
        PING_PIC,
        caption=caption,
        parse_mode="html",
        link_preview=False
    )
    return await event.delete()
