from telegram import Update
from telegram.ext import ContextTypes
from database import user_exists
from gpt_predictor import generate_prediction

async def predict_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = str(update.message.from_user.id)
    username = update.message.from_user.username or "voyageur"

    if not user_exists(telegram_id):
        await update.message.reply_text("🔒 Tu dois t'inscrire d'abord avec /register.")
        return

    await update.message.reply_text("🔮 Je scrute les étoiles... un instant...")
    prediction = generate_prediction(username)
    await update.message.reply_text(prediction)
