import telebot
import os

ADMIN_ID = "8153082299"  # Xavfsiz solishtirish uchun str ko'rinishida
USERS_FILE = "bot_users.txt"

# Asosiy menyu tugmalari
main_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_keyboard.add(
    "🐶 Tasodifiy It", "🐱 Tasodifiy Mushuk",
    "🔢 Tasodifiy Son", "🛒 Savatchani Ko'rish",
    "➕ Savatga Qo'shish", "🧹 Savatni Tozalash"
)

def save_user_details(user_id, first_name, username):
    """Foydalanuvchini faylga chiroyli formatda saqlash"""
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            pass

    with open(USERS_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    
    id_exists = False
    for line in lines:
        if f"ID: {user_id}" in line:
            id_exists = True
            break
            
    if not id_exists:
        user_username = f"@{username}" if username else "Nikneym yo'q"
        with open(USERS_FILE, "a", encoding="utf-8") as f:
            f.write(f"ID: {user_id} | Ism: {first_name} | Nik: {user_username}\n")

def register_start_handlers(bot: telebot.TeleBot):
    
    @bot.message_handler(commands=['start'])
    def cmd_start(message):
        uid = message.from_user.id
        first_name = message.from_user.first_name
        username = message.from_user.username
        
        save_user_details(uid, first_name, username)
        
        welcome_text = (
            f"👋 Assalomu alaykum, {first_name}!\n\n"
            f"🤖 Random Botga xush kelibsiz!\n\n"
            f"Bu bot orqali siz tasodifiy it va mushuk rasmlarini ko'rishingiz, "
            f"hamda tasodifiy sonlar generatsiya qilishingiz mumkin.\n\n"
            f"👇 Boshlash uchun quyidagi tugmalardan birini bosing:"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=main_keyboard)

    @bot.message_handler(commands=['statistika'])
    def cmd_statistika(message):
        if str(message.from_user.id) == str(ADMIN_ID):
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, "r", encoding="utf-8") as f:
                    users_list = f.read().splitlines()
                
                users_count = len(users_list)
                
                if users_count > 0:
                    report_text = f"📊 **Bot statistikasi:**\n👥 Jami foydalanuvchilar: {users_count} ta\n\n"
                    report_text += "📝 **Foydalanuvchilar ro'yxati:**\n"
                    for num, user in enumerate(users_list, 1):
                        report_text += f"{num}. {user}\n"
                    bot.send_message(message.chat.id, report_text, parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id, "📊 Botda hali foydalanuvchilar yo'q.")
            else:
                bot.send_message(message.chat.id, "📊 Botda hali foydalanuvchilar yo'q.")
        else:
            bot.send_message(message.chat.id, "❌ Bu buyruq faqat bot admini uchun!")