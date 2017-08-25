import os
from functools import partial

SELECTED_LANGUAGE = os.getenv('LANGUAGE', 'EN')

MESSAGES = {
    'RU': {
        'intro': "Привет! Я знаю все заведения в округе.",
        'need_coordinates': "<b>Название</b>: {}.\n<b>куда топать</b>: {}\n<b>сколько топать</b>: {} метров\n<b>рейтинг</b>: {}.\n<a href='{}'>Показать на КАРТЕ</a>",
        'not_indicated': "не указано",
        'coordinates_are_required': "Необходимы координаты.",
        'not_found': "Нет ничего такого поблизости :(",
        'search': "Найти заведение"
    },
    'EN': {
        'intro': "Hello! I know all the places in the district.",
        'need_coordinates': "<b>Title</b>: {}.\n<b>where to stomp</b>: {}\n<b>how much to stamp</b>: {} meters\n<b>rating</b>: {}\n<a href='{}'>Show on the MAP</a>",
        'not_indicated': "not indicated",
        'coordinates_are_required': "Coordinates are required.",
        'not_found': "There's nothing nearby :(",
        'search': "Find an institution"
    }
}


def get_message(language, messages, key):
    return messages[language][key]


get_message_by_key = partial(partial(get_message, SELECTED_LANGUAGE), MESSAGES)
