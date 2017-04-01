from pyfcm import FCMNotification
from database import Database
import query_formats


class FCMSender:
    def __init__(self, server_key):
        self.push_service = FCMNotification(api_key=server_key)
        self.db = Database()

    def send(self, title, message):
        registration_ids = list() # DB에서 가져오는 클라이언트 id들
        clients_to_push = self.get_clients_to_push(registration_ids, self.db)
        message_title = title
        message_body = message

        result = self.push_service.notify_multiple_devices(registration_ids=clients_to_push,
                                                           message_title=message_title,
                                                           message_body=message_body)

        return result

    @staticmethod
    def get_clients_to_push(registration_ids, db):
        rows = db.execute(query_formats.get_registration_id_format)
        clients_to_push = list()
        for row in rows:
            clients_to_push.append(row['registration_key'])

        print(clients_to_push)
        return clients_to_push

sender = FCMSender('AAAA9LkX9Zs:APA91bHyu886FvO46OzqQLkBofJfxpszMI9_HpBrMTPkTed46hzsColH0K9sloVNRaiRwszAn17eDPfue5-KtzS0Q0gPekTgyzRa1CjgbpBathxpD6OH0lsj8CHDJVt8DDRQuVu8_Xjh')
sender.send('푸쉬푸쉬', '히히히')