from pyfcm import FCMNotification

push_service = FCMNotification(api_key='AIzaSyDEqNM3DgDvmxryb2pDrjry5wLHuT8NPjI')

result = push_service.notify_topic_subscribers(message_title='Helpable',
                                               message_body='미국엔 장애인이 없다고!!!.',
                                               message_icon='../splash_back.png',
                                               topic_name='all')

print(result)
