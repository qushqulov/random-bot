import telebot
import random
import requests

def register_random_handlers(bot: telebot.TeleBot):

    @bot.message_handler(func=lambda message: message.text == "🐶 Tasodifiy It")
    def send_random_dog(message):
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random").json()
            dog_url = response.get("message")
            bot.send_photo(message.chat.id, dog_url, caption="🐶 Siz uchun tasodifiy it rasmi!")
        except Exception:
            bot.send_message(message.chat.id, "❌ It rasmini yuklashda xatolik yuz berdi.")

    @bot.message_handler(func=lambda message: message.text == "🐱 Tasodifiy Mushuk")
    def send_random_cat(message):
        try:
            response = requests.get("https://api.thecatapi.com/v1/images/search").json()
            cat_url = response[0].get("url")
            bot.send_photo(message.chat.id, cat_url, caption="🐱 Siz uchun tasodifiy mushuk rasmi!")
        except Exception:
            bot.send_message(message.chat.id, "❌ Mushuk rasmini yuklashda xatolik yuz berdi.")

    @bot.message_handler(func=lambda message: message.text == "🔢 Tasodifiy Son")
    def send_random_number(message):
        random_num = random.randint(1, 100)
        bot.send_message(message.chat.id, f"🔢  Sizning tasodifiy soningiz: **{random_num}**", parse_mode="Markdown")