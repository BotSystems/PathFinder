from handlers.messages import get_message_by_key


class Place():
    name = None
    location = None
    direction = None
    distance = None
    rating = None

    def __init__(self, name, location, direction, distance, rating):
        self.name = name
        self.location = location
        self.direction = direction
        self.distance = distance
        self.rating = rating

    def get_answer_message_template(self):
        return get_message_by_key('need_coordinates')

    def build_answer(self):
        answer = self.get_answer_message_template()
        return answer.format(self.name, self.location, self.distance, self.rating, self.direction)
