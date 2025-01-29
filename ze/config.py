from decouple import config
from ast import literal_eval

version = "1.0.0"

class Config:
    def __getattr__(self, __name: str):
        if __name in self.__dict__:
            return self.__dict__[__name]
        _data = config(__name, default="")
        try:
            return literal_eval(_data)
        except Exception:
            return _data

    API_ID = config("API_ID", cast=int, default=6)
    API_HASH = config("API_HASH", default="fe77fbf0cae9f7f5ece37659e2466cf1")

Var = Config = Config()
