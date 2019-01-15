from django.conf import settings

BASE_URL = 'http://api.sendcloud.net/apiv2'

SEND_CLOUD_DEFAULTS = {
    # "send_mail": "{base_url}/mail/send".format(base_url=BASE_URL),
    # "mail_template_send": "{base_url}/mail/sendtemplate".format(base_url=BASE_URL),

    "spark_key": {
        "APP_USER": "fake_user",
        "APP_KEY": "fake_key",
    },
    "batch_key": {
        "APP_USER": "fake_user",
        "APP_KEY": "fake_key",
    },

    "mail": {
        "send_mail": "{base_url}/mail/send".format(base_url=BASE_URL),
        "send_template": "{base_url}/mail/sendtemplate".format(base_url=BASE_URL),
        "send_calendar": "{base_url}/mail/sendcalendar".format(base_url=BASE_URL),
        "task_info": "{base_url}/mail/taskinfo".format(base_url=BASE_URL),
    },

    "template": {
        "list": "{base_url}/template/list".format(base_url=BASE_URL),
        "get": "{base_url}/template/get".format(base_url=BASE_URL),
        "add": "{base_url}/template/add".format(base_url=BASE_URL),
        "delete": "{base_url}/template/delete".format(base_url=BASE_URL),
        "update": "{base_url}/template/update".format(base_url=BASE_URL),
    },

    "member": {
        "list": "{base_url}/addressmember/list".format(base_url=BASE_URL),
        "get": "{base_url}/addressmember/get".format(base_url=BASE_URL),
        "add": "{base_url}/addressmember/add".format(base_url=BASE_URL),
        "update": "{base_url}/addressmember/update".format(base_url=BASE_URL),
        "delete": "{base_url}/addressmember/delete".format(base_url=BASE_URL),
    },

}

send_cloud_config = SEND_CLOUD_DEFAULTS.copy()


def get_send_cloud_setting(sc_config):

    send_cloud_config.update(
        getattr(settings, "SEND_CLOUD_KEY", {})
    )

    return send_cloud_config.get(sc_config)


def get_send_cloud_spark_user():
    _spark = get_send_cloud_setting('spark_key')
    return _spark.get('APP_USER')


def get_send_cloud_spark_key():
    _spark = get_send_cloud_setting('spark_key')
    return _spark.get('APP_KEY')


def get_send_cloud_batch_user():
    _batch = get_send_cloud_setting('batch_key')
    return _batch.get('APP_USER')


def get_send_cloud_batch_key():
    _batch = get_send_cloud_setting('batch_key')
    return _batch.get('APP_KEY')


# ----------------------------------------------------------------------------------------------------------------------
def get_mail_config(kind="send_mail"):
    _mail = get_send_cloud_setting("mail")
    return _mail.get(kind)


def get_send_mail_url():
    return get_mail_config()


def get_template_send():
    return get_mail_config(kind="send_template")


def get_send_calendar():
    return get_mail_config(kind="send_calendar")


def get_task_info():
    return get_mail_config(kind="task_info")


# ----------------------------------------------------------------------------------------------------------------------
def get_template_config(kind="list"):
    _template = get_send_cloud_setting("template")
    return _template.get(kind)


def get_template_list():
    return get_template_config()


def get_template():
    return get_template_config(kind='get')


def add_template():
    return get_template_config(kind="add")


def delete_template():
    return get_template_config("delete")


def update_template():
    return get_template_config("update")


# ----------------------------------------------------------------------------------------------------------------------
def get_member_config(kind="list"):
    _member = get_send_cloud_setting("member")
    return _member.get(kind)


def member_list():
    return get_member_config()
    # return get_send_cloud_setting("member_list")


def member_get():
    return get_member_config(kind='get')
    # return get_send_cloud_setting("member_get")


def member_add():
    return get_member_config(kind='add')
    # return get_send_cloud_setting("member_add")


def member_update():
    return get_member_config(kind='update')
    # return get_send_cloud_setting("member_update")


def member_delete():
    return get_member_config(kind='delete')
    # return get_send_cloud_setting("member_delete")


if __name__ == "__main__":
    print(get_send_mail_url())
    print(get_template_send())
    print(get_send_calendar())
    print(get_task_info())
