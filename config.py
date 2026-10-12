from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "93c6f3c43ede0082aceebfff185cf5ff")
      API_ID = int(getenv("API_ID", "18013154"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8668760056:AAGzRndPpjzNVJ2GC-9yyxGe4CYNPCByv6o")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1004411647916:-1004411647916").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
