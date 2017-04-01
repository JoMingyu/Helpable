from pyfcm import FCMNotification

push_service = FCMNotification(api_key='AIzaSyDEqNM3DgDvmxryb2pDrjry5wLHuT8NPjI')

result = push_service.notify_topic_subscribers(message_body='asdfasdfasdf',
                                               topic_name='all')

print(result)