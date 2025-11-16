import telebot
from telebot import types
import json

config = json.load(open("config.json", "r"))
bot = telebot.TeleBot(config["TOKEN"])
admin = config["ADMIN"]

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("📢 Free Promotions Group", url=config["GROUP_LINK"]))
    bot.send_message(message.chat.id,
    f"👋 Welcome {message.from_user.first_name}!\n\n"
    f"📌 This bot allows channel owners to get FREE promotion exchanges.\n"
    f"💠 Add this bot as admin in your channel\n"
    f"💠 Send your channel link to get instant exchange partners.\n\n"
    f"🔥 Bot Name: FREE UPI INSTANT", reply_markup=kb)

@bot.message_handler(func=lambda m: True)
def handle(message):
    if "t.me/" in message.text:
        bot.send_message(admin, f"🚨 New channel submitted:\n{message.text}")
        bot.send_message(message.chat.id, "📌 Your channel received. You will get an exchange partner soon 🔥")
    else:
        bot.send_message(message.chat.id, "🔗 Send channel link only.")

bot.polling()
