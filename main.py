import telebot

API_KEY = "5299193377:AAHEGIBIqtPeqVcnJ6GiQcteofe0W4GrmF8"

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

@bot.message_handler(commands=["/sagar"])
def send_start(inf):
    bot.reply_to(inf,"[29/05, 7:24 pm] Sagar: Eno nindhu
[29/05, 7:24 pm] Sagar: En madtha udya
[29/05, 7:24 pm] Sagar: Idya*
[29/05, 7:24 pm] Sagar: Yalla odbuta")

bot.polling()
