import telebot
from handlers.start import main_keyboard

USER_CARTS = {}
USER_STATES = {}

def register_cart_handlers(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda m: m.text == "🛒 Savatchani Ko'rish")
    def view_cart(message):
        user_id = message.from_user.id
        savat = USER_CARTS.get(user_id, [])
        if not savat:
            bot.send_message(message.chat.id, "Sizning savatchangiz bo'sh!")
        else:
            text = "Sizning savatchangizdagi mahsulotlar:\n\n" + "\n".join([f"- {item}" for item in savat])
            bot.send_message(message.chat.id, text)

    @bot.message_handler(func=lambda m: m.text == "➕ Savatga Qo'shish")
    def add_start(message):
        USER_STATES[message.from_user.id] = "kutish"
        bot.send_message(message.chat.id, "Savatchaga qo'shmoqchi bo'lgan mahsulot nomini yozing:")

    @bot.message_handler(func=lambda m: m.text == "🧹 Savatni Tozalash")
    def clear_cart(message):
        USER_CARTS[message.from_user.id] = []
        bot.send_message(message.chat.id, "Sizning savatchangiz tozalandi.")

    # Foydalanuvchi mahsulot nomini yozib yuborganda ushlab qoladigan funksiya
    @bot.message_handler(func=lambda m: USER_STATES.get(m.from_user.id) == "kutish")
    def add_save(message):
        user_id = message.from_user.id
        mahsulot = message.text.strip()
        
        if user_id not in USER_CARTS:
            USER_CARTS[user_id] = []
        
        USER_CARTS[user_id].append(mahsulot)
        USER_STATES[user_id] = None  # Holatni bo'shatamiz
        bot.send_message(message.chat.id, f"'{mahsulot}' savatchaga qo'shildi!", reply_markup=main_keyboard)