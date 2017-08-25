# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from dotenv import load_dotenv
from telegram.ext import Updater

from handlers.handler import init_handlers

dotenv_path = join(dirname(__file__), '.env.settings')
load_dotenv(dotenv_path)

if __name__ == '__main__':
    updater = Updater(token=os.getenv('TOKEN'))
    dispatcher = init_handlers(updater.dispatcher)
    updater.start_polling()
    updater.idle()
