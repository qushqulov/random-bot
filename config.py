import os
from dotenv import load_dotenv

# .env faylini o'qishni boshlaydi
load_dotenv()

# .env ichidagi BOT_TOKEN kalitiga mos keluvchi qiymatni oladi
BOT_TOKEN = os.getenv("BOT_TOKEN")