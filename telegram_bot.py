import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from llm import ask_llm
from config import TELEGRAM_PDD_BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Реакция на команду /start."""
    await update.message.reply_text("Привет! Я бот и тд...")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Реакция на любое обычное текстовое сообщение."""
    user_input = update.message.text                 # входная переменная
    await update.message.chat.send_action("typing")  # "печатает..." в чате

    answer = ask_llm(user_input)                     # выходная переменная

    await update.message.reply_text(answer)


app = ApplicationBuilder().token(TELEGRAM_PDD_BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
