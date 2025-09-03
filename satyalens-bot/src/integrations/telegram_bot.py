import sys
import os
# Add project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from src.core.chatbot import SatyaLensBot

load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

config = {
    'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    'GOOGLE_SAFE_BROWSING_API_KEY': os.getenv('GOOGLE_SAFE_BROWSING_API_KEY'),
    'ARYA_AI_API_KEY': os.getenv('ARYA_AI_API_KEY'),
    'URLVOID_API_KEY': os.getenv('URLVOID_API_KEY'),
    'VIRUSTOTAL_API_KEY': os.getenv('VIRUSTOTAL_API_KEY')
}

bot_core = SatyaLensBot(config)

async def start(update, context):
    await update.message.reply_text("Hi! Send me any URL and I'll analyze it.")

async def handle_message(update, context):
    user_message = update.message.text
    chat_id = update.message.chat.id
    response = bot_core.process_message(str(chat_id), 'telegram', user_message)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Telegram bot is running...")  # <-- Add this line
    app.run_polling()

if __name__ == '__main__':
    main()

