from django.conf import settings
from sendcloud import APIBaseClass
from .conf import (
    get_template_send,
    get_template,
    add_template,
    delete_template,
    update_template,
)
#
# send_cloud_v2_template_api = {
#     "template_send": "http://api.sendcloud.net/apiv2/mail/sendtemplate",
#     "template_get": "http://api.sendcloud.net/apiv2/template/get",
#     "template_add": "http://api.sendcloud.net/apiv2/template/add",
#     "template_delete": "http://api.sendcloud.net/apiv2/template/delete",
#     "template_update": "http://api.sendcloud.net/apiv2/template/update",
# }


class SendCloudTemplate(APIBaseClass):

    def __init__(self, invoke_name, fail_silently=False, *args, **kwargs):
        _edm_user = kwargs.pop('edm_user', None)
        self.invoke_name = invoke_name
        try:
            self._edm_user = _edm_user or getattr(settings, 'MAIL_EDM_USER')
        except AttributeError:
            if fail_silently:
                self._edm_user = None
            else:
                raise

        self.get_url = get_template()
        self.add_url = add_template()
        self.update_url = update_template()
        self.send_url = get_template_send()
        self.delete_url = delete_template()
        super(SendCloudTemplate, self).__init__(*args, **kwargs)

    @property
    def edm_user(self):
        return self._edm_user

    def get_or_create(self, **kwargs):
        if not self.get_status():
            self.add(**kwargs)

    def update_or_create(self, **kwargs):
        if not self.get_status():
            self.add(**kwargs)
        else:
            self.update(**kwargs)

    def get_status(self):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'invokeName': self.invoke_name
        }

        res = self.post_api(self.get_url, data)

        if len(res['templateList']) == 0:
            return False
        try:
            template_info = res['templateList'][0]
            return template_info['is_verify']
        except Exception:
            if not self.fail_silently:
                raise
            return False

    def add(self, name, html, subject, email_type=1):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'invokeName': self.invoke_name,
            'name': name,
            'html': html,
            'subject': subject,
            'templateType': email_type
        }
        return self.post_api(self.add_url, data)

    def update(self, name, html, subject, email_type=1):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'invokeName': self.invoke_name,
            'name': name,
            'html': html,
            'subject': subject,
            'templateType': email_type
        }
        return self.post_api(self.update_url, data)

    def delete(self):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'invokeName': self.invoke_name,
        }
        res = self.post_api(self.delete_url, data)
        return res

    def send_to_list(self, subject, from_mail, from_name, to):
        data = {
            'apiUser': self.edm_user,
            'apiKey': self.api_key,
            'useAddressList': 'true',
            'resp_email_id': 'true',
            'templateInvokeName': self.invoke_name,
            'subject': subject,
            'to': to,
            "from": from_mail,
            # "mail_from": from_mail,
            "fromName": from_name,
        }
        return self.post_api(self.send_url, data)
