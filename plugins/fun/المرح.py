"""
**❃ جميع هذه الاوامر تستخدم بالرد على الشخص عدا أمر كت**

❃ `{i}رفع مطي`
❃ `{i}رفع كلب`
❃ `{i}رفع حيوان`
❃ `{i}رفع زاحف`
❃ `{i}رفع مرتي`
❃ `{i}رفع زوجي`
❃ `{i}رفع تاج`
❃ `{i}رفع بكلبي`
❃ `{i}رفع بزون`
❃ `{i}رفع قرد`

❃ `{i}نسبة الحب`
❃ `{i}نسبة الانوثة`
❃ `{i}نسبة الرجولة`
❃ `{i}نسبة الغباء`
❃ `{i}نسبة المثلية`

❃ `{i}كت`
❃ `{i}اوصف`
❃ `{i}هينه`
❃ `{i}نزوج`
❃ `{i}طلاك`"""

import random

from ze.helper import get_uinfo
from resources.fun import *

from .. import *


@ze_cmd(pattern="رفع بكلبي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بڪلبك 🖤 "
    )


@ze_cmd(pattern="رفع زوجي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \nتـم رفعه زوجج روحوا خلفوا 🤤😂",
    )


@ze_cmd(pattern="رفع مطي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**⌔∮ دي هذا مطور السورس أبتعد**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفـعه مطي هـنا "
    )


@ze_cmd(pattern="رفع مرتي(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه مـࢪتك مـشي نخـلف 😹🤤",
    )


@ze_cmd(pattern="رفع كلب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return

    if user.id == 6929438980:
        return await eor(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه جلب خليه خله ينبح 😂🐶",
    )


@ze_cmd(pattern="كت(?: |$)(.*)")
async def mention(mention):
    kt = random.choice(kattwet)
    await eor(mention, f"**- {kt}**")


@ze_cmd(pattern="هينه(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 1694386561:
        return await eor(mention, f"**⌔∮ أبتعد هذا صديق المطور لا**")
    if user.id == 6929438980:
        return await eor(mention, f"**- لكك دي هذا المطور**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(hena)
    await eor(mention, f"{sos} .")


@ze_cmd(pattern="نسبة الحب(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    moh = random.choice(nsba)
    await eor(
        mention, f"نـسـبتكم انـت و [{muh}](tg://user?id={user.id}) هـي {moh} 😔🖤"
    )


@ze_cmd(pattern="نسبة الانوثة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**- لكك دي هذا المطور زلمة وعلى راسك**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(rr7)
    await eor(
        mention, f"- نسبة الانوثة لـ [{muh}](tg://user?id={user.id}) هي {sos} 🥵🖤"
    )


@ze_cmd(pattern="نسبة الغباء(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zebot = random.choice(rr7)
    await eor(
        mention, f"نسبة الغباء لـ [{muh}](tg://user?id={user.id}) هـي {zebot} 😂💔"
    )


@ze_cmd(pattern="رفع تاج(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه تاج 👑🔥"
    )


@ze_cmd(pattern="رفع قرد(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**- لكك دي هذا المطور**")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention,
        f"- المستخدم [{tag}](tg://user?id={user.id}) \n تـم رفعـه قرد واعطائه موزة 🐒🍌",
    )


@ze_cmd(pattern="اوصف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    zebot = random.choice(Describe)
    await eor(mention, f"{zebot}")


@ze_cmd(pattern="شغله(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    rezw = random.choice(jobtype)
    await eor(
        mention, f"- المستخدم [{muh}](tg://user?id={user.id}) شغله هو {rezw}"
    )


@ze_cmd(pattern="نسبة الرجولة(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**⌔∮ نسبة رجولة مودي مالك السورس هي 100%**")
    muh = user.first_name.replace("\u2060", "") if user.first_name else user.username
    sos = random.choice(kz)
    await eor(
        mention, f"- نسبة الرجولة لـ [{muh}](tg://user?id={user.id}) هـي {sos} 🥵🖤"
    )


@ze_cmd(pattern="رفع حيوان(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه حيوان 🐏"
    )


@ze_cmd(pattern="رفع بزون(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه بزون 🐈"
    )


@ze_cmd(pattern="رفع زاحف(?: |$)(.*)")
async def permalink(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if custom:
        return await eor(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await eor(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🐍💞"
    )

@ze_cmd(pattern="نزوج(?: |$)(.*)")
async def wiffun(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await eor(mention, f"**نزوج وماتباوع على غيري 🥺💞 ܰ**")

@ze_cmd(pattern="طلاك(?: |$)(.*)")
async def mention(mention):
    user, custom = await get_uinfo(mention)
    if not user:
        return
    if user.id == 6929438980:
        return await eor(mention, f"**⌔∮ عذرا هذا مطور السورس**")
    await eor(mention, f"**طالق طالق بالعشرة 😹😭💕 ܰ**")
