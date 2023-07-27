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
    
def button(update: Update, context: CallbackContext) -> None:
    update.callback_query.answer()
    update.callback_query.message.edit_reply_markup(
    reply_markup=InlineKeyboardMarkup([])
    )
    if update.callback_query.data == 'eng':
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(f'''Hello {update.effective_user.first_name} \U0001F44B, I am capable of converting text to speech \U0001F50A. In order to use the function, click on /english command please.\n
\U0001F4CC Important note: if you are going to insert a long text (over 3000 characters) --> keep in mind that telegram divides such messages into shorter ones and sends them separately.\n
\U00002757 This is important because I can convert only the first message you send, so you will need to repeat the function /english as many times as the number of messages you have for conversion.''')
    elif update.callback_query.data == 'pol':
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(f'''Cześć {update.effective_user.first_name} \U0001F44B, potrafię tekst przekształcić w format audio \U0001F50A. Aby skorzystać z tej funkcji naciśnij tutaj --> /polish\n
\U0001F4CC Ważne: jeśli planujesz wysłać dużą wiadomość tekstową (ponad 3000 liter) --> pamiętaj, że telegram dzieli takie duże wiadomości na mniejsze i są one wysyłane osobno.\n
\U00002757 To jest istotne, ponieważ jestem w stanie przekonwertować tylko pierszą wiadomość, którą wysyłasz, dlatego będziesz musiał użyć funkcji /polish dla każdej osobnej wiadomości, wysłanej przez ciebie.''')
    elif update.callback_query.data == 'ukr':
        update.callback_query.message.delete()
        update.callback_query.message.reply_text(f'''Привіт {update.effective_user.first_name} \U0001F44B, я вмію конвертувати текст в аудіо формат \U0001F50A. Щоб скористатися функцією натисни ---> /ukrainian\n
\U0001F4CC Важливо: якщо ти плануєш надіслати дійсно довге текстове повідомлення (понад 3000 символів) --> пам\'ятай, що телеграм автоматично ділить великі повідомлення на менші і надсилає їх окремо.\n
\U00002757 Це важливо, оскільки що я можу конвертувати тільки перше надіслане повідомлення, тому функцію /ukrainian потрібно буде повторити для кожного окремо надісланого повідомлення.''')
    
def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('stop', stop))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()