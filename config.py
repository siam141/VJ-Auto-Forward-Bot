from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "67d3ec64db8031189962b5d4804884c0")
      API_ID = int(getenv("API_ID", "27752560"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7728598881:AAF3evUl3YJw9dp4wm58Ad0oZu1CbeWgMMo")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002530980008:-1002589776901").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
