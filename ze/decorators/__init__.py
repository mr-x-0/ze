from contextlib import suppress
from database import zedB
from .manager import eod, eor


StatsHolder = {}

def should_allow_sudos():
    return zedB.get_key("SUDO")


def get_sudos() -> list:
    return zedB.get_key("SUDOS") or []


def is_sudo(userid):
    return userid in get_sudos()


def owner_and_sudos(only_full=False):
    if only_full:
        return [zedB.get_config("OWNER_ID"), *fullsudos()]
    return [zedB.get_config("OWNER_ID"), *get_sudos()]


def _parse(key):
    with suppress(TypeError):
        return int(key)
    return key


def fullsudos():
    fullsudos = []
    if sudos := zedB.get_key("FULLSUDO"):
        fullsudos.extend(str(sudos).split())
    owner = zedB.get_config("OWNER_ID")
    if owner and owner not in fullsudos:
        fullsudos.append(owner)
    return list(map(_parse, filter(lambda id: id, fullsudos)))
