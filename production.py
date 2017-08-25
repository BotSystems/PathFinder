import os

import telegram
from flask import Flask, request
from telegram.ext import Dispatcher

from handlers.handler import init_handlers

app = Flask(__name__)
bot = telegram.Bot(os.getenv('TOKEN'))
dispatcher = init_handlers(Dispatcher(bot, None, workers=0))


@app.route('/' + os.getenv('TOKEN'), methods=['GET', 'POST'])
def webhook_handler():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok!'


if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    debug = os.getenv('DEBUG')

    app.run(host='0.0.0.0', port=port, debug=debug)
