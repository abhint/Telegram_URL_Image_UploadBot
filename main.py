#!/usr/bin/env python3
# This is bot coded by Abhijith-cloud and used for educational purposes only
# https://github.com/Abhijith-cloud
# (c) Abhijith N T ;-)
# Thank you https://github.com/pyrogram/pyrogram :-)

from pyrogram import Client
from config import my
plugins = dict(
        root="plugins"
    )
bot = Client(
    "Image upload bot",
    bot_token = my.BOT_TOKEN,
    api_id = my.API_ID,
    api_hash = my.API_HASH,
    plugins = plugins
)
bot.run()




# from pyrogram import Client
# plugins = dict(
#         root="plugins"
#     )
# bot = Client(
#     "Image Uploading Bot",
#     bot_token = '1306098991:AAGgo3F2AoTCrpYtU1gaAyvI2J7nxcqvkwg',
#     api_id = 1427768,
#     api_hash = 'be224f7cf30ad49c481198d7fb010983',
#     plugins = plugins
# )

# bot.run()