"""
❃ `{i}لوك`
    لـ عرض اخر أسطر من عملية التنصيب وعرض سجل العمليات
    
❃ `{i}اعادة تشغيل`
    لـ اعادة تشغيل سورس زد إي ( الافضل تستخدمه في مجموعة الحفظ )
    
❃ `{i}تحديث`
    لـ تحديث سورس زد إي اذا كان هنالك تحديث جديد ولمعرفة التحديثات تابع @SOURCEZE
"""


import os
import sys
import time
from ze.helper.git import repo
from ze.helper import check_update, bash, get_client
from .. import zedB, ze_cmd


@ze_cmd(pattern="لوك( (.*)|$)")
async def logs_ze(event):
    arg = event.pattern_match.group(1).strip()

    file_path = "ze.log"
    if not arg: 
        with open(file_path, "r") as file:
            content = file.read()[-4000:]
        return await event.eor(f"`{content}`")
    elif arg == "تلجراف":
        client = get_client()
        with open(file_path, "r") as file:
            title = "Ze Logs"
            page = client.create_page(title=title, content=[file.read()])
        await event.eor(f'[Ze Logs]({page["url"]})', link_preview=True)
    await event.eor(file=file_path)


@ze_cmd(pattern="اعادة تشغيل$")
async def restart_ze(event):
    await event.eor("⌔∮ جار اعادة تشغيل سورس زد إي سيتم تنبيهك في مجموعة الحفظ بعد تشغيل السورس أنتظر فقط")
    os.execl(sys.executable, sys.executable, "-m", "ze")

@ze_cmd(pattern="تحديث( (.*)|$)")
async def update_ze(e):
    xx = await e.eor("**⌔∮ جار البحث عن تحديثات لسورس زد إي**")
    cmd = e.pattern_match.group(1).strip()
    if cmd and ("سريع" in cmd or "خفيف" in cmd):
        await bash("git pull -f")
        await xx.edit("**⌔∮ جار التحديث الخفيف يرجى الأنتظار**")
        os.execl(sys.executable, sys.executable, "-m", "ze")
    remote_url = repo.get_remote_url()
    if remote_url.endswith(".git"):
        remote_url = remote_url[:-4]
    m = check_update()
    if not m:
        return await xx.edit(
            f'<strong>سورس زد إي مُحدث بأخر أصدار</strong>',
            parse_mode="html",
            link_preview=False,
        )
    msg = await xx.eor(
        f'<strong>جـار تحديث سورس زد إي يرجى الأنتظار قليلا</strong>',
        parse_mode="html",
        link_preview=False,
    )
    await update(msg)


async def update(eve):
    await bash(f"git pull && {sys.executable} -m pip install -r requirements.txt")
    os.execl(sys.executable, sys.executable, "-m", "ze")
