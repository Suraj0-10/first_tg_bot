from pyrogram import Client, filters
from pyrogram.types import ChatPermissions
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
bot = Client("bot",
            api_id = 5168062,
            api_hash = "04c049aa96d1cc87920b45b7fb43c0d0",
            bot_token = "5261660867:AAE6JWmiwg65idb0KR0tuyyHwpeNGpDprBQ"
            )
@bot.on_message(filters.command("start"))
def cmd1(bot,message):
 bot.send_message(message.chat.id,"hi")
#button
START_MESSAGE = "MY CHANNELS"
START_MESSAGE_BUTTON = [
  [InlineKeyboardButton
   ('MOVIES',url='t.me/PX_07')
  ],
  [InlineKeyboardButton
   ('SERIES',url='t.me/seriez_encoded')
  ]
]
@bot.on_message(filters.command("channel"))
def channel(bot,message):
 text = START_MESSAGE
 reply_markup =  InlineKeyboardMarkup(START_MESSAGE_BUTTON)
 message.reply(
  text = text,
  reply_markup = reply_markup,
  )
#welcome message
GROUP = "-1001662127173"
WLCM = "Hey! Welcome to my group!😳"
@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcome(client, message):
   message.reply_text(WLCM)
#@bot.on_message(filters.text)
#def cmd1(client,message):
 #message.reply_text(message.text)
#print("started")
bot.run()
