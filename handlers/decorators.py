# -*- coding: utf-8 -*-

from models import Chanel


def save_chanel_decorator(fn):
    def wrapper(bot, update, *args, **kwargs):
        print('SAVE CHANEL')

        try:
            if (update.callback_query):
                chat_id = update.callback_query.message.chat.id
                first_name = update.callback_query.message.chat.first_name
                last_name = update.callback_query.message.chat.last_name
            else:
                chat_id = update.message.chat.id
                first_name = update.message.chat.first_name
                last_name = update.message.chat.last_name

            defaults = {'chanel_id': chat_id, 'first_name': first_name, 'last_name': last_name}
            chanel, is_new = Chanel.get_or_create(chanel_id=chat_id, defaults=defaults)
            chanel.update_me()
        except Exception as ex:
            print(ex)

        return fn(bot, update, *args, **kwargs)

    return wrapper
