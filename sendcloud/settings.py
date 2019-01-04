from django.conf import settings as djsettings

BASE_URL = "http://api.sendcloud.net/apiv2"

send_cloud_app_user = getattr(djsettings, 'MAIL_APP_USER')
send_cloud_app_key = getattr(djsettings, 'MAIL_APP_KEY')

SEND_CLOUD = {
    "send_mail": "{base_url}/mail/send",
    "sendtemplate": "{base_url}/mail/sendtemplate",
}

send_cloud_config = SEND_CLOUD.copy()


send_cloud_config.update({
    "app_user": send_cloud_app_user,
    "app_key": send_cloud_app_key,
})

