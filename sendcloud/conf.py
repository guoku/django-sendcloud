from django.conf import settings

BASE_URL = "http://api.sendcloud.net/apiv2"

SEND_CLOUD_DEFAULTS = {
    # "send_mail": "{base_url}/mail/send".format(base_url=BASE_URL),
    # "mail_template_send": "{base_url}/mail/sendtemplate".format(base_url=BASE_URL),
    "spark_key": {"APP_USER": "fake_user", "APP_KEY": "fake_key"},
    "batch_key": {"APP_USER": "fake_user", "APP_KEY": "fake_key"},
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
    "address_list": {
        "list": "{base_url}/addresslist/list".format(base_url=BASE_URL),
        "add": "{base_url}/addresslist/add".format(base_url=BASE_URL),
        "delete": "{base_url}/addresslist/delete".format(base_url=BASE_URL),
        "update": "{base_url}/addresslist/update".format(base_url=BASE_URL),
    },
    "member": {
        "list": "{base_url}/addressmember/list".format(base_url=BASE_URL),
        "get": "{base_url}/addressmember/get".format(base_url=BASE_URL),
        "add": "{base_url}/addressmember/add".format(base_url=BASE_URL),
        "update": "{base_url}/addressmember/update".format(base_url=BASE_URL),
        "delete": "{base_url}/addressmember/delete".format(base_url=BASE_URL),
    },
    "user_info": {"get": "{base_url}/userinfo/get".format(base_url=BASE_URL)},
    "api_user": {
        "list": "{base_url}/apiuser/list".format(base_url=BASE_URL),
        "add": "{base_url}/apiuser/add".format(base_url=BASE_URL),
    },
    "analytics": {
        "status": "{base_url}/data/emailStatus".format(base_url=BASE_URL),
        "invalid_stat": "{base_url}/invalidstat/list".format(base_url=BASE_URL)
    },
}

send_cloud_config = SEND_CLOUD_DEFAULTS.copy()


def get_send_cloud_setting(sc_config):
    send_cloud_config.update(getattr(settings, "SEND_CLOUD_KEY", {}))

    return send_cloud_config.get(sc_config)


def get_send_cloud_spark_user():
    _spark = get_send_cloud_setting("spark_key")
    return _spark.get("APP_USER")


def get_send_cloud_spark_key():
    _spark = get_send_cloud_setting("spark_key")
    return _spark.get("APP_KEY")


def get_send_cloud_batch_user():
    _batch = get_send_cloud_setting("batch_key")
    return _batch.get("APP_USER")


def get_send_cloud_batch_key():
    _batch = get_send_cloud_setting("batch_key")
    return _batch.get("APP_KEY")


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


# send cloud template url
# ----------------------------------------------------------------------------------------------------------------------
def get_template_config(kind="list"):
    _template = get_send_cloud_setting("template")
    return _template.get(kind)


def get_template_list():
    return get_template_config()


def get_template():
    return get_template_config(kind="get")


def add_template():
    return get_template_config(kind="add")


def delete_template():
    return get_template_config("delete")


def update_template():
    return get_template_config("update")


# send cloud address list url
# ----------------------------------------------------------------------------------------------------------------------
def get_address_list_config(kind="list"):
    _address_list = get_send_cloud_setting("address_list")
    return _address_list.get(kind)


def address_list():
    return get_address_list_config()


def address_add():
    return get_address_list_config(kind="add")


def address_update():
    return get_address_list_config(kind="update")


def address_delete():
    return get_address_list_config(kind="delete")


# send cloud member url
# ----------------------------------------------------------------------------------------------------------------------
def get_member_config(kind="list"):
    _member = get_send_cloud_setting("member")
    return _member.get(kind)


def member_list():
    return get_member_config()
    # return get_send_cloud_setting("member_list")


def member_get():
    return get_member_config(kind="get")
    # return get_send_cloud_setting("member_get")


def member_add():
    return get_member_config(kind="add")
    # return get_send_cloud_setting("member_add")


def member_update():
    return get_member_config(kind="update")
    # return get_send_cloud_setting("member_update")


def member_delete():
    return get_member_config(kind="delete")
    # return get_send_cloud_setting("member_delete")


# ----------------------------------------------------------------------------------------------------------------------
def get_user_info_url():
    _info = get_send_cloud_setting("user_info")
    return _info.get("get")


def api_user_list_url():
    _info = get_send_cloud_setting("api_user")
    return _info.get("list")


def api_user_add_url():
    _info = get_send_cloud_setting("api_user")
    return _info.get("add")


#
# http://www.sendcloud.net/doc/email_v2/stats_do/#_3
# ----------------------------------------------------------------------------------------------------------------------
def get_invalid_stat_url():
    _analytics = get_send_cloud_setting("analytics")
    return _analytics.get("invalid_stat")


#
# http://www.sendcloud.net/doc/email_v2/deliver_response/
# ----------------------------------------------------------------------------------------------------------------------
def get_email_status():
    _status = get_send_cloud_setting("analytics")
    return _status.get("status")


if __name__ == "__main__":
    print(get_send_mail_url())
    print(get_template_send())
    print(get_send_calendar())
    print(get_task_info())
