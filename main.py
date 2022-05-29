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

N1 = 1
N2 = 3
Sum = N1 + N2
print(sum)
@bot.message_handler(commands=["sum"])
def send_start(inf):
    bot.reply_to(inf,"sum")


bot.polling()
