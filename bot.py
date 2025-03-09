import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставляем ваш токен от BotFather
TOKEN = "7742101855:AAHx2LdPVN3i8vWmdCWmQky7TjA-RW_jAys"

# Включаем логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: CallbackContext) -> None:
    """Функция приветствия при старте"""
    await update.message.reply_text("Привет! Я DPO_LectureBot. Введите /generate, чтобы создать лекцию.")

def main():
    """Запуск бота"""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
