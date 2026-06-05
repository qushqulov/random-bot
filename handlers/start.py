import telebot

# Bot menyusi uchun pastki tugmalarni yasaymiz
main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row("🐶 Tasodifiy It", "🐱 Tasodifiy Mushuk")
main_keyboard.row("🔢 Tasodifiy Son", "🛒 Savatchani Ko'rish")
main_keyboard.row("➕ Savatga Qo'shish", "🧹 Savatni Tozalash")

def register_start_handlers(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def cmd_start(message):
        bot.send_message(
            message.chat.id, 
            "Random Botga xush kelibsiz! Quyidagi menyudan birini tanlang:", 
            reply_markup=main_keyboard
        )