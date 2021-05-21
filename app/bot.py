import re
import telegram
from flask import Flask, request
from credentials import TOKEN, URL
from telegram import Update
from app import get_price_change



global bot
global TOKEN
bot = telegram.Bot(token=TOKEN)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   
   if text == "/get_px":
       price_change = get_price_change()
       bot.sendMessage(chat_id=chat_id, text=price_change, reply_to_message_id=msg_id)


   else:
       bot.sendMessage(chat_id=chat_id, text="There was a problem in the name you used, please enter different name", reply_to_message_id=msg_id)

   return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    # we use the bot object to link the bot to our app which lives
    # in the link provided by URL
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    # something to let us know things work
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    

@app.route('/')
def index():
   return '.'

