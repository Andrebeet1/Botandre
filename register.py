from telegram import Update
from telegram.ext import ContextTypes
from database import add_user, user_exists

async def register_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = str(update.message.from_user.id)
    username = update.message.from_user.username or "Anonyme"

    if user_exists(telegram_id):
        await update.message.reply_text("📝 Tu es déjà inscrit.")
    else:
        add_user(telegram_id, username)
        await update.message.reply_text(f"✅ Bienvenue {username} ! Tu es maintenant inscrit.")

async def login_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = str(update.message.from_user.id)
    if user_exists(telegram_id):
        await update.message.reply_text("🔐 Connexion réussie.")
    else:
        await update.message.reply_text("❌ Tu n'es pas encore inscrit. Utilise /register.")
