import asyncio
import sys
from random import randint

from telethon.errors import (
    ChannelsTooMuchError,
    ChatAdminRequiredError,
    UserNotParticipantError,
)

from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    InviteToChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon import Button
from telethon.tl.types import (
    ChatAdminRights,
    ChatPhotoEmpty,
    InputChatUploadedPhoto
)
from telethon.utils import get_peer_id
from ze.helper import inline_mention#, check_update
from ze import LOGS

async def inline_on():
    from .. import tgbot, zedB, zeubot
    if zedB.get_key("INLINE_SET"):
        return
    bot = "BotFather"
    await zeubot.send_message(bot, "/setinline")
    await asyncio.sleep(1)
    await zeubot.send_message(bot, f"@{tgbot.me.username}")
    await asyncio.sleep(1)
    await zeubot.send_message(bot, "Search")
    await zeubot.send_read_acknowledge(bot)
    zedB.set_key("INLINE_SET", True)


async def notify():
    from .. import tgbot, zedB, zeubot
    chat_id = zedB.get_key("LOG_CHAT")
    spam_sent, BTTS = None, None
    
    if not zedB.get_key("FIRST_DEPLOY"):
        MSG = f"🎇 **مرحبًا بك في سورس زد إي أكتمل التنصيب بنجاح** \n\n✨ **استعد لاستكشاف الميزات الجديدة!**  \n💭 إليك بعض الخيارات التي ستساعدك في التعرف على سورس زد إي واستخدامه بفعالية:  \n   - تعلم كيفية استخدام الأوامر الأساسية.  \n   - استكشاف الوظائف المختلفة المتاحة.  \n   - الانضمام إلى مجموعة الدعم للحصول على المساعدة والتوجيه.  \n\n📩 نحن هنا لدعمك، فلا تتردد في طرح أي سؤال أو استفسار!"
        PHOTO = "resources/Ze.jpg"
        BTTS = Button.inline("• أضغط هنا للبدأ •", "initft_2")
        zedB.set_key("FIRST_DEPLOY", True)
    else:
        MSG = f"🌟 تنصيب سورس زد إي أكتمل بنجاح! ☑️\n\n👤 **حساب المالك:** {inline_mention(zeubot.me)}\n🤖 **البوت المساعد:** @{tgbot.me.username}\n\n📩 نرحب بك في مجموعتنا! إذا كان لديك أي استفسارات فلا تتردد في السؤال!\n💬 **مجموعة المساعدة:** @ZESUPORT"
        BTTS, PHOTO = None, None

        if prev_spam := zedB.get_key("LAST_UPDATE_LOG_SPAM"):
            try:
                await tgbot.delete_messages(chat_id, int(prev_spam))
            except Exception:
                pass
    try:
        spam_sent = await tgbot.send_message(chat_id, MSG, file=PHOTO, buttons=BTTS)
    except Exception as el:
        LOGS.exception(el)
        try:
            spam_sent = await zeubot.send_message(chat_id, MSG)
        except Exception as ef:
            LOGS.exception(ef)
    if spam_sent:
        zedB.set_key("LAST_UPDATE_LOG_SPAM", spam_sent.id)


async def group_ub():
    from .. import tgbot, zedB, zeubot

    log_chat = zedB.get_key("LOG_CHAT")
    new_channel = None
    if log_chat:
        try:
            chat = await zeubot.get_entity(log_chat)
        except BaseException as err:
            LOGS.exception(err)
            zsdB.del_key("LOG_CHAT")
            log_chat = None
    if not log_chat:
        async def _save(exc):
            zedB._cache["LOG_CHAT"] = zeubot.me.id
            await tgbot.send_message(
                zeubot.me.id, f"حدث خطأ في انشاء مجموعة الحفظ الخطأ: {exc}.\n حاليا الرسائل المحفوظة هي بديل مجموعة الحفظ."
            )
        LOGS.info("جار صنع مجموعة الحفظ يرجى الأنتظار")
        try:
            group_id = await zeubot(
                CreateChannelRequest(
                    title="مجموعة الحفظ لزد إي",
                    about="مجموعة حفظ الأحداث والتنبيهات الخاصة بسورس زد إي\n\n انضم لقناة السورس @SOURCEZE",
                    megagroup=True,
                ),
            )
        except ChannelsTooMuchError as er:
            LOGS.critical(
                "يبدو انك موجود في العديد من المجموعات او القنوات غادر بعضها و قم بأعادة تشغيل السورس"
            )
            return await _save(str(er))
        except BaseException as er:
            LOGS.exception(er)
            LOGS.info(
                "لقد حدث خطأ ما يرجى صنع مجموعة و وضع الايدي الخاص بها مع المتغير LOG_CHAT."
            )

            return await _save(str(er))
        new_channel = True
        chat = group_id.chats[0]
        log_chat = get_peer_id(chat)
        zedB.set_key("LOG_CHAT", log_chat)
    assistant = True
    try:
        await zeubot.get_permissions(int(log_chat), tgbot.me.username)
    except UserNotParticipantError:
        try:
            await zeubot(InviteToChannelRequest(int(log_chat), [tgbot.me.username]))
        except BaseException as er:
            LOGS.info("لقد حدث خطأ اثناء اضافة البوت المساعد الى مجموعة الحفظ")
            LOGS.exception(er)
            assistant = False
    except BaseException as er:
        assistant = False
        LOGS.exception(er)
    if assistant and new_channel:
        try:
            achat = await tgbot.get_entity(int(log_chat))
        except BaseException as er:
            achat = None
            LOGS.info("حدث خطأ اثناء تعرف البوت المساعد على مجموعة الحفظ")
            LOGS.exception(er)
        if achat and not achat.admin_rights:
            rights = ChatAdminRights(
                add_admins=True,
                invite_users=True,
                change_info=True,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
                anonymous=False,
                manage_call=True,
            )
            try:
                await zeubot(
                    EditAdminRequest(
                        int(log_chat), tgbot.me.username, rights, "البوت المساعد"
                    )
                )
            except ChatAdminRequiredError:
                LOGS.info(
                    "لقد حدث خطأ اثناء رفع البوت المساعد الى مشرف يبدو انك لا تمتلك صلاحيات كافية'"
                )
            except BaseException as er:
                LOGS.info("لقد حدث خطأ اثناء رفع البوت المساعد في مجموعة الحفظ..")
                LOGS.exception(er)
    if isinstance(chat.photo, ChatPhotoEmpty):
        pic = await zeubot.upload_file(file="resources/Ze.jpg")
        try:
            await zeubot(EditPhotoRequest(int(log_chat), pic))
        except BaseException as er:
            LOGS.exception(er)



async def tag_chat():
    from .. import tgbot, zedB, zeubot

    tag_chat = zedB.get_key("TAG_CHAT")
    new_tag = None
    if tag_chat:
        try:
            chat = await zeubot.get_entity(tag_chat)
        except BaseException as err:
            LOGS.exception(err)
            zedB.del_key("TAG_CHAT")
            tag_chat = None
    if not tag_chat:
        LOGS.info("جار صنع مجموعة التخزين يرجى الأنتظار")
        try:
            group_id = await zeubot(
                CreateChannelRequest(
                    title="مجموعة التخزين لزد إي",
                    about="مجموعة تخزين الرسائل الخاصة بك\n\n انضم لقناة السورس @SOURCEZE",
                    megagroup=True,
                ),
            )
        except ChannelsTooMuchError as er:
            LOGS.critical(
                "يبدو انك موجود في العديد من المجموعات او القنوات غادر بعضها و قم بأعادة تشغيل السورس"
            )
        except BaseException as er:
            LOGS.exception(er)
            LOGS.info(
                "لقد حدث خطأ ما يرجى صنع مجموعة و وضع الايدي الخاص بها مع المتغير TAG_CHAT."
            )

        new_tag = True
        chat = group_id.chats[0]
        tag_chat = get_peer_id(chat)
        zedB.set_key("TAG_CHAT", tag_chat)
    assistant = True
    try:
        await zeubot.get_permissions(int(tag_chat), tgbot.me.username)
    except UserNotParticipantError:
        try:
            await zeubot(InviteToChannelRequest(int(tag_chat), [tgbot.me.username]))
        except BaseException as er:
            LOGS.info("خطأ في اضافة البوت المساعد الى مجموعة التخزين")
            LOGS.exception(er)
            assistant = False
    except BaseException as er:
        assistant = False
        LOGS.exception(er)
    if assistant and new_tag:
        try:
            achat = await tgbot.get_entity(int(tag_chat))
        except BaseException as er:
            achat = None
            LOGS.info("حدث خطأ اثناء التعرفة على مجموعة التخزين من قبل البوت المساعد")
            LOGS.exception(er)
        if achat and not achat.admin_rights:
            rights = ChatAdminRights(
                add_admins=True,
                invite_users=True,
                change_info=True,
                ban_users=True,
                delete_messages=True,
                pin_messages=True,
                anonymous=False,
                manage_call=True,
            )
            try:
                await zeubot(
                    EditAdminRequest(
                        int(tag_chat), tgbot.me.username, rights, "البوت المساعد"
                    )
                )
            except ChatAdminRequiredError:
                LOGS.info(
                    "لقد حدث خطأ اثناء رفع البوت المساعد الى مشرف يبدو انك لا تمتلك صلاحيات كافية'"
                )
            except BaseException as er:
                LOGS.info("لقد حدث خطأ اثناء رفع البوت المساعد في مجموعة التخزين..")
                LOGS.exception(er)
    if isinstance(chat.photo, ChatPhotoEmpty):
        pic = await zeubot.upload_file(file="resources/Ze.jpg")
        try:
            await zeubot(EditPhotoRequest(int(tag_chat), pic))
        except BaseException as er:
            LOGS.exception(er)


async def main_process():
    await inline_on()
    await group_ub()
    await tag_chat()
    await notify()
