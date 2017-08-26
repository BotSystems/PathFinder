# -*- coding: utf-8 -*-
import os

from telegram.ext import MessageHandler, CommandHandler

from handlers.core import send_places, get_nearby_places, take_by_limit, order_places, build_places, build_keyboard

from handlers.messages import get_message_by_key
from handlers.decorators import save_chanel_decorator

GOOGLE_PLACE_LIMIT = os.getenv('GOOGLE_PLACE_LIMIT')
GOOGLE_PLACE_TOKEN = os.getenv('GOOGLE_PLACE_TOKEN')
GOOGLE_PLACE_TYPE = os.getenv('GOOGLE_PLACE_TYPE')
GOOGLE_PLACE_DISTANCE = os.getenv('GOOGLE_PLACE_DISTANCE')


@save_chanel_decorator
def handle_start(bot, update):
    message = get_message_by_key('intro')
    update.message.reply_text(message, reply_markup=build_keyboard())


@save_chanel_decorator
def handle_coordinate(bot, update):
    try:
        if not update.message.location:
            return update.message.reply_text(get_message_by_key('coordinates_are_required'))

        lat, lng = update.message.location.latitude, update.message.location.longitude
        nearby_places = get_nearby_places(lat, lng, GOOGLE_PLACE_TOKEN, GOOGLE_PLACE_TYPE, GOOGLE_PLACE_DISTANCE)
        places_objects = take_by_limit(order_places(build_places(nearby_places, lat, lng)), int(GOOGLE_PLACE_LIMIT))

        return send_places(update, places_objects)
    except Exception as ex:
        print(ex)


def init_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', handle_start))
    dispatcher.add_handler(MessageHandler(None, handle_coordinate))
    return dispatcher
