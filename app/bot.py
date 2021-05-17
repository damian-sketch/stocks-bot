import os


from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    ConversationHandler,
    Filters
)

from telegram import Update
from app import get_price_change
import logging

PORT = int(os.environ.get("PORT", 443))
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


# what your bot should reply when we send the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def get_px_change(update, context):

    message = get_price_change()
    update.message.reply_text(message)

    # the main function, with some boilerplate
def main():
    updater = Updater(token= TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', get_price_change)
    px_handler = CommandHandler('get_px', get_px_change)
    dispatcher.add_handler(start_handler) # this line is what matters most
    dispatcher.add_handler(px_handler)
    # updater.start_polling()

    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN
    )
    updater.bot.setWebhook("https://marketsbot101.herokuapp.com/" + TOKEN)
    
    updater.idle()
    

if __name__ == "__main__":
    main()
