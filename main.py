from keep_alive import keep_alive
import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Halo! Ini LeoBot aktif 24 jam 😎")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Kamu kirim: {message.text}")

keep_alive()
bot.polling()
