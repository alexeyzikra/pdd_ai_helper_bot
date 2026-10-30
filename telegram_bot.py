import os
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

    try:
        answer = ask_llm(user_input)                 # выходная переменная
    except Exception as e:
        print("Ошибка:", e)
        answer = f'Что-то пошло не так, сообщите в поддержку (@maths_enjoyer) эту ошибку "{e}"'

    for part in split_text(answer):
        await update.message.reply_text(part)

def split_text(text, limit=4000):
    parts = []
    while len(text) > limit:
        cut = text.rfind("\n", 0, limit)
        if cut == -1:
            cut = limit
        parts.append(text[:cut])
        text = text[cut:].lstrip("\n")
    parts.append(text)

    return parts


def main():
    app = ApplicationBuilder().token(TELEGRAM_PDD_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()