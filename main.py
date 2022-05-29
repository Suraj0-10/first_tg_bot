import telebot
API_KEY = "5299193377:AAHEGIBIqtPeqVcnJ6GiQcteofe0W4GrmF8"

bot = telebot.TeleBot(API_KEY,parse_mode=None)
@bot.message_handler(commands=["start"])
def send_start(strt):
    bot.reply_to(strt,"bsdk")
bot.polling()
