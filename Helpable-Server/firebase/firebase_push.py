from pyfcm import FCMNotification
from database import Database
import query_formats


class FCMSender:
    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)

    def send(self, title, message, registration_id=None):
        message_title = title
        message_body = message

        if registration_id is None:
            result = self.push_service.notify_topic_subscribers(topic_name='all',
                                                                message_title=message_title,
                                                                message_body=message_body)
        else:
            result = self.push_service.notify_single_device(registration_id=registration_id,
                                                            message_body=message_body,
                                                            message_title=message_title)

        print(result)
        return result

    @staticmethod
    def get_clients_to_push():
        rows = Database().execute(query_formats.get_registration_id_format)
        clients_to_push = list()
        for row in rows:
            clients_to_push.append(row['registration_key'])

        return clients_to_push
