#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# (c) Abhijith N T
# Thank you https://github.com/pyrogram/pyrogram 

from pyrogram import Client
from config import config
plugins = dict(
        root="plugins"
    )
bot = Client(
    "Image upload bot",
    bot_token = config.BOT_TOKEN,
    api_id = config.API_ID,
    api_hash = config.API_HASH,
    plugins = plugins
)
bot.run()
