"""
❃ `{i}تحميل صوتي` <(رابط يوتيوب/او اي رابط)>
   لـ تحميل الملف بشكل ملف صوتي في التليجرام، يمكنك وضع رابط اي منصة


❃ `{i}تحميل فيد` <(رابط يوتيوب/او اي رابط)>
   لـ تحميل الملف بشكل فيديو في التليجرام، يمكنك وضع رابط اي منصة


❃ `{i}صوتي` <(عنولن)>
   لـ تحميل الملف بشكل ملف صوتي في التليجرام من خلال العنوان فقط بدون رابط

"""

from .. import download_yt, get_yt_link, is_url_work, ze_cmd

ytd = {
        "prefer_ffmpeg": True,
        "addmetadata": True,
        "geo-bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegMetadata"}],
    }

@ze_cmd(pattern="تحميل صوتي (.*)")
async def down_voic(event):
    zebot = await event.eor("⌔∮ جار التحميل يرجى الأنتظار قليلا")
    ytd["format"] = "bestaudio"
    ytd["outtmpl"] = "%(id)s.m4a"
    ytd["postprocessors"].insert(
            0,
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
                "preferredquality": "128",
            },
        )
    url = event.pattern_match.group(1)
    if not url:
        return await zebot.eor("⌔∮ يجب عليك وضع رابط للتحميل الصوتي")
    try:
        await is_url_work(url)
    except BaseException:
        return await zebot.eor("⌔∮ يرجى وضع الرابط بشكل صحيح")
    await download_yt(zebot, url, ytd)

@ze_cmd(pattern="تحميل فيد (.*)")
async def vidown(event):
    zebot = await event.eor("⌔∮ جار التحميل يرجى الأنتظار قليلا")
    ytd["format"] = "best"
    ytd["outtmpl"] = "%(id)s.mp4"
    ytd["postprocessors"].insert(
        0, {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
        )
    url = event.pattern_match.group(1)
    print(url)
    if not url:
        return await zebot.eor("⌔∮ يجب عليك وضع رابط لتحميل الفيد")
    try:
        await is_url_work(url)
    except BaseException:
        return await zebot.eor("⌔∮ يرجى وضع الرابط بشكل صحيح")
    await download_yt(zebot, url, ytd)


@ze_cmd(pattern="صوتي( (.*)|$)")
async def sotea(event):
    zebot = await event.eor("⌔∮ جار التحميل يرجى الأنتظار قليلا")
    ytd["format"] = "bestaudio"
    ytd["outtmpl"] = "%(id)s.m4a"
    ytd["postprocessors"].insert(
        0,
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
            "preferredquality": "128",
        },
    )
    query = event.pattern_match.group(2) if event.pattern_match.group(1) else None
    if not query:
        return await zebot.eor("**⌔∮ يجب عليك تحديد ما تريد تحميله اكتب عنوان مع الامر**")
    url = get_yt_link(query, ytd)
    if not url:
        return await zebot.edit("**⌔∮ لم يتم العثور على الفيديو اكتب عنوان مفصل بشكل صحيح**")
    await zebot.eor("**⌔∮ جار تحميل الملف الصوتي أنتظر قليلا**")
    await download_yt(zebot, url, ytd)


