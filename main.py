import telebot
from config import BOT_TOKEN
# Barcha handlerlarni fayllaridan import qilamiz
from handlers.start import register_start_handlers
from handlers.randoms import register_random_handlers
from handlers.cart import register_cart_handlers

# Botni yaratish
bot = telebot.TeleBot(BOT_TOKEN)

# Handlerlarni botga ulash (Ketma-ketlik buzilmasligi shart)
register_start_handlers(bot)
register_random_handlers(bot)
register_cart_handlers(bot)

if __name__ == "__main__":
    print("Bot muvaffaqiyatli ishga tushdi...")
    
    # 409 Conflict xatosini majburlab yo'qotish
    bot.remove_webhook()
    
    # Botni ishga tushirish
    bot.polling(none_stop=True)