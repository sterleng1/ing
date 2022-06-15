## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME",BQBpKqJffvEn_Xk6m1_7OszU9XLSnuL_Z5hwcKVKt-rn6eYDYmi0HVnt4HdVi5spydF2MUmyRBGLfGgkZeOkJlIEL2tVryxkZN9rmcMwFIT_DrASY51-7o2Cc9N6fhRFmt2akTuj6Fh06Ym6VACS3IuuklAgHKChTFXr4YqlOTKMtDjUI6KcfToElozNZ42zCI3LIYH0uV4K5FuwzLaKK4BMCkbFYAdfT529jj4zRUCy9nzg9jZkmuKpOa2RhCpQKmf5dJrRh57i5TU27-bfzqhCzSp_OVgvdvrqKKb5XhUvPq5Dvv-nngdpCFHB69fQlcIHu_XHjBtz28B6JTNX3Lt_AAAAAUQHfDMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5352960649:AAFlPJ7v9BMwnz0tA6d-joyqwGHdF3Jc1qw")
BOT_NAME = getenv("BOT_NAME", "TOTA")
API_ID = int(getenv("API_ID", "17680868"))
API_HASH = getenv("API_HASH", "f3a473574fdc7dcdfdfc9398f6052ce1")
OWNER_NAME = getenv("OWNER_NAME", "BODY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "B_O_D_Y9")
ALIVE_NAME = getenv("ALIVE_NAME", "BODY")
BOT_USERNAME = getenv("BOT_USERNAME", "BODYX11BOT")
OWNER_ID = getenv("OWNER_ID", "5382011688")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BODY")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "B_O_D_Y6")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "B_O_D_Y7")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
