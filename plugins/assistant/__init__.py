from telethon.tl.types import InputWebDocument

from ze import tgbot
from ze.decorators.asstbot import tgbot_cmd, callback, in_pattern

from .. import Button, inline_pic, inline_mention, up_catbox

AST_PLUGINS = {}

def get_back_button(name):
    return [Button.inline("رجوع", data=f"{name}")]


@in_pattern(owner=True, func=lambda x: not x.text)
async def inline_alive(o):
    TLINK = inline_pic() or "https://telegra.ph/file/41a777f089288f7ad2571.jpg"
    MSG = "• ** سورس زد إي •**"
    WEB0 = InputWebDocument(
        "https://telegra.ph/file/41a777f089288f7ad2571.jpg", 0, "image/jpg", []
    )
    RES = [
        await o.builder.article(
            type="photo",
            text=MSG,
            include_media=True,
            buttons=[
                [
                    Button.url(
                        "قناة السورس", url="https://T.me/SOURCEZE"
                    ),
                    Button.url("مجموعة المساعدة", url="t.me/ZESUPORT"),
                ],
            ],
            title="سورس زد إي",
            description="🔱 𝐒𝐎𝐔𝐑𝐂𝐄 𝐙𝐄 🔱 | زد إي",
            url=TLINK,
            thumb=WEB0,
            content=InputWebDocument(TLINK, 0, "image/jpg", []),
        )
    ]
    await o.answer(
        RES,
        private=True,
        cache_time=300,
        switch_pm="👥 Ze",
        switch_pm_param="start",
    )
