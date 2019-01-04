
BASE_URL = "http://api.sendcloud.net/apiv2"

SEND_CLOUD = {
    "send_mail": "{base_url}/mail/send".format(base_url=BASE_URL),
    "sendtemplate": "{base_url}/mail/sendtemplate".format(base_url=BASE_URL),
}

send_cloud_config = SEND_CLOUD.copy()


def get_send_cloud_setting(settings):
    return send_cloud_config.get(settings)


def get_send_mail_url():

    return get_send_cloud_setting('send_mail')

