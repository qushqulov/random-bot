import telebot
from config import BOT_TOKEN
from handlers.start import register_start_handlers
from handlers.randoms import register_random_handlers
from handlers.cart import register_cart_handlers

# Botni tokenga ulaymiz
bot = telebot.TeleBot(BOT_TOKEN)

# Bo'lingan fayllardagi funksiyalarni botga tanitamiz
register_start_handlers(bot)
register_random_handlers(bot)
register_cart_handlers(bot)  # Bu eng oxirida turishi shart

if __name__ == "__main__":
    print("Mening professional botim ishga tushdi...")
    bot.infinity_polling()