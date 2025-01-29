from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import InputPeerNotifySettings

async def join_dev():
    from .. import zeubot
    try:
        await zeubot(UnblockRequest("@D_S_IS"))
        await zeubot(
                UpdateNotifySettingsRequest(
                peer="t.me/D_S_IS",
                settings=InputPeerNotifySettings(mute_until=2**31 - 1),
            )
        )
        channel_usernames = [
            "SOURCEZE",
            "F0R_MODY",
            "ZESUPORT"
        ]
        for channel_username in channel_usernames:
            try:
                channel = await zeubot.get_entity(channel_username)
                await zeubot(JoinChannelRequest(channel=channel))
            except Exception as e:
                LOGS.error(f"{e}")
    except BaseException:
        pass
