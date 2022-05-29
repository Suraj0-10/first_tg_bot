import telebot

API_KEY = "5261660867:AAE6JWmiwg65idb0KR0tuyyHwpeNGpDprBQ"

bot = telebot.TeleBot(API_KEY,parse_mode=None)
@bot.message_handler(commands=["start"])
def send_start(strt):
    bot.reply_to(strt,"Hey! I'm a test or Practice bot of @Zoro_to\nYou can try out my commands\n/help\n/info\n/start")

@bot.message_handler(commands=["help"])
def send_start(hlp):
    bot.reply_to(hlp,"There's nothing to help ask @zoro_to he may help u")

@bot.message_handler(commands=["info"])
def send_start(inf):
    bot.reply_to(inf,"Basically @zoro_to made this bot to test new codes and run it ")

@bot.message_handler(commands=["text"])
def send_start(inf):
    bot.reply_to(inf,"none")

@bot.message_handler(commands=["aj"])
def send_start(inf):
    bot.reply_to(inf,"thanks @anime_in_30mb for this amazing channel\nI hope u do well in exams @Assassin_Aj")

bot.polling()
