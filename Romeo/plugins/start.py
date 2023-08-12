import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *
from Romeo import app
from config import *

MESSAGE = """
❥︎ 𝐒𝐓𝐀𝐑𝐓 ☟︎︎︎

𝐇𝐞𝐥𝐥𝐨, 
𝐈'𝐦 𝐚 𝐑𝐨𝐦𝐞𝐨 
𝐔𝐬𝐞𝐫𝐁𝐨𝐭 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐇𝐞𝐫𝐞.
"""

#start
@app.on_message(filters.command("start", ["/", ".", "!", "?"]) & filters.private)
async def start(client, message):

 #  await message.reply_text("Hey RomeoBot Assistant here")

   buttons = [
            [
                InlineKeyboardButton("• 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 •", url="t.me/RomeoBot_op"),
            ],
            [
                InlineKeyboardButton("• 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="t.me/Romeo_op"),
            ],
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   await client.send_photo(message.chat.id, photo=ALIVE_PIC, caption=MESSAGE, reply_markup=reply_markup)
