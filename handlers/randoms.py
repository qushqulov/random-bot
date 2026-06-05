import random
import telebot
from utils.api import get_random_dog, get_random_cat

def register_random_handlers(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda m: m.text == "🐶 Tasodifiy It")
    def send_dog(message):
        url = get_random_dog()
        if url:
            bot.send_photo(message.chat.id, url, caption="Mana sizga tasodifiy kuchukcha!")
        else:
            bot.send_message(message.chat.id, "Rasm yuklashda xatolik bo'ldi.")

    @bot.message_handler(func=lambda m: m.text == "🐱 Tasodifiy Mushuk")
    def send_cat(message):
        url = get_random_cat()
        if url:
            bot.send_photo(message.chat.id, url, caption="Mana sizga tasodifiy mushukcha!")
        else:
            bot.send_message(message.chat.id, "Rasm yuklashda xatolik bo'ldi.")

    @bot.message_handler(func=lambda m: m.text == "🔢 Tasodifiy Son")
    def send_number(message):
        son = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Sizning tasodifiy soningiz (1-100): *{son}*", parse_mode="Markdown")