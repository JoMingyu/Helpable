from pyfcm import FCMNotification
from database import Database
import query_formats


class FCMSender:
    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)
        self.db = Database()

    def send(self, title, message, registration_id=None):
        if registration_id is None:
            clients_to_push = self.get_clients_to_push(self.db)
        else:
            clients_to_push = registration_id

        message_title = title
        message_body = message

        result = self.push_service.notify_multiple_devices(registration_ids=clients_to_push,
                                                           message_title=message_title,
                                                           message_body=message_body)

        return result

    @staticmethod
    def get_clients_to_push(db):
        rows = db.execute(query_formats.get_registration_id_format)
        clients_to_push = list()
        for row in rows:
            clients_to_push.append(row['registration_key'])

        return clients_to_push
