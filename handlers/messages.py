import os
from functools import partial

MESSAGES = {
    'RU': {
        'need_coordinates': "<b>Название</b>: {}.\n<b>куда топать</b>: {}\n<b>сколько топать</b>: {} метров\n<b>рейтинг</b>: {}.\n<a href='{}'>Показать на КАРТЕ</a>",
        'not_indicated': "не указано",
        'coordinates_are_required': "Coordinates are required.",
        'not_found': "Нет ничего такого поблизости :("
    },
    'EN': {
        'need_coordinates': "<b>Title</b>: {}.\n<b>where to stomp</b>: {}\n<b>how much to stamp</b>: {} meters\n<b>rating</b>: {}\n<a href='{}'>Show on the MAP</a>",
        'not_indicated': "not indicated",
        'coordinates_are_required': "Необходимы координаты.",
        'not_found': "There's nothing nearby :("
    }
}

selected_language = os.getenv('LANGUAGE', 'RU')


def get_message(language, messages, key):
    return messages[language][key]


get_message_by_key = partial(partial(get_message, selected_language), MESSAGES)
