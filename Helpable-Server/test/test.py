from pyfcm import FCMNotification

push_service = FCMNotification(api_key='AIzaSyDEqNM3DgDvmxryb2pDrjry5wLHuT8NPjI')

result = push_service.notify_topic_subscribers(message_title='Helpable',
                                               message_body='이세인님에게 도움이 필요합니다.',
                                               message_icon='../splash_back.png',
                                               topic_name='all')

print(result)