import telebot
import os

# هات التوكن من المتغير البيئي (مش تكتبه ثابت جوه الكود)
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلا بيك في بوت *إمبراطور الأنمي*!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"إنت كتبت: {message.text}")

print("🤖 البوت شغال...")

bot.infinity_polling()
