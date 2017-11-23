import datetime
from base_client import BaseClient


class Friends(BaseClient):
    class FriendsNotFound(Exception):
        @staticmethod
        def msg():
            print('Friends not found')

    method = 'friends'
    http_method = 'get'

    def __init__(self, uid):
        self.uid = uid

    def get_params(self):
        return {'user_id': self.uid, 'fields': 'bdate'}

    def response_handler(self, response):
        friends = response.json().get('response')
        if not friends:
            raise self.FriendsNotFound

        ages = []
        today = datetime.datetime.today()
        c = []

        for friend in friends:
            date = friend.get('bdate')

            try:
                dt = datetime.datetime.strptime(date, '%d.%m.%Y')
            except TypeError:
                continue
            except ValueError:
                continue

            age = today.year - dt.year
            if today.month < dt.month:
                age -= 1
            elif today.month == dt.month and today.day < dt.day:
                age -= 1

            ages.append(age)




        return ages
