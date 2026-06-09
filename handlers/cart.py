import telebot
from handlers.start import main_keyboard

USER_CARTS = {}
USER_STATES = {}

def register_cart_handlers(bot: telebot.TeleBot):
    @bot.message_handler(func=lambda m: m.text in ["🛒 Savatchani Ko'rish", "➕ Savatga Qo'shish", "🧹 Savatni Tozalash"])
    def handle_cart_buttons(message):
        uid = message.from_user.id
        
        if message.text == "🛒 Savatchani Ko'rish":
            savat = USER_CARTS.get(uid, [])
            text = "Sizning savatchangiz bo'sh!" if not savat else "Savat:\n" + "\n".join([f"- {i}" for i in savat])
            bot.send_message(message.chat.id, text)
            
        elif message.text == "➕ Savatga Qo'shish":
            USER_STATES[uid] = "kutish"
            bot.send_message(message.chat.id, "Mahsulot nomini yozing:")
            
        elif message.text == "🧹 Savatni Tozalash":
            USER_CARTS[uid] = []
            bot.send_message(message.chat.id, "Savat tozalandi.")

    # Mahsulot nomini saqlash
    @bot.message_handler(func=lambda m: USER_STATES.get(m.from_user.id) == "kutish")
    def add_save(message):
        uid = message.from_user.id
        USER_CARTS.setdefault(uid, []).append(message.text.strip())
        USER_STATES[uid] = None
        bot.send_message(message.chat.id, "Qo'shildi!", reply_markup=main_keyboard)