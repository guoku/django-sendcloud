BASE_URL = "http://api.sendcloud.net/apiv2"

SEND_CLOUD = {
    "send_mail": "{base_url}/mail/send".format(base_url=BASE_URL),
    "mail_template_send": "{base_url}/mail/sendtemplate".format(base_url=BASE_URL),
    "mail_template_list": "{base_url}/template/list".format(base_url=BASE_URL),
    "mail_template_get": "{base_url}/template/get".format(base_url=BASE_URL),
    "mail_template_add": "{base_url}/template/add".format(base_url=BASE_URL),
    "mail_template_delete": "{base_url}/template/delete".format(base_url=BASE_URL),
    "mail_template_update": "{base_url}/template/update".format(base_url=BASE_URL),
}

send_cloud_config = SEND_CLOUD.copy()


def get_send_cloud_setting(settings):
    return send_cloud_config.get(settings)


def get_send_mail_url():
    return get_send_cloud_setting("send_mail")


def get_template_send():
    return get_send_cloud_setting("mail_template_send")


def get_template_list():
    return get_send_cloud_setting("mail_template_list")


def get_template():
    return get_send_cloud_setting("mail_template_get")


def add_template():
    return get_send_cloud_setting("mail_template_add")


def delete_template():
    return get_send_cloud_setting("mail_template_delete")


def update_template():
    return get_send_cloud_setting("mail_template_update")
