from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from telegram.chataction import ChatAction
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()
PORT = int(os.environ.get('PORT', 5000))
APIKEY = os.environ.get('APIKEY')
TOKEN = APIKEY

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    reply_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("English \U0001F1EC\U0001F1E7", callback_data='eng')],
        [InlineKeyboardButton("Polish \U0001F1F5\U0001F1F1", callback_data='pol')],
        [InlineKeyboardButton("Ukrainian \U0001F1FA\U0001F1E6", callback_data='ukr')],
    ])
    update.message.reply_text('Please select a language:',
    reply_markup=reply_buttons)

def stop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bot is on pause \U000023F8\nUse /start or /help in order to\nuse the bot again.")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""


Available commands:

/start --> Restart a bot
/help --> Available commands
/english --> Convert in English
/polish --> Convert in Polish
/ukrainian --> Convert in Ukrainian
""")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()