from telegram import Update
from telegram.ext import ContextTypes
from database import is_admin, get_all_users

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = str(update.message.from_user.id)

    if not is_admin(telegram_id):
        await update.message.reply_text("⛔ Accès refusé. Tu n'es pas admin.")
        return

    users = get_all_users()
    if not users:
        await update.message.reply_text("Aucun utilisateur enregistré.")
    else:
        msg = "👥 Utilisateurs inscrits :\n\n"
        for username, tid in users:
            msg += f"• @{username} (ID: {tid})\n"
        await update.message.reply_text(msg)
