# from django.conf import settings
# from sendcloud import APIBaseClass
# from .exceptions import SendCloudAPIError
# from .conf import (
#     get_template_send,
#     get_template,
#     add_template,
#     delete_template,
#     update_template,
# )
#
#
# class SendCloudTemplate(APIBaseClass):
#
#     def __init__(self, invoke_name, fail_silently=False, *args, **kwargs):
#         _edm_user = kwargs.pop('edm_user', None)
#         self.invoke_name = invoke_name
#         try:
#             self._edm_user = _edm_user or getattr(settings, 'MAIL_EDM_USER')
#         except AttributeError:
#             if fail_silently:
#                 self._edm_user = None
#             else:
#                 raise
#
#         self.get_url = get_template()
#         self.add_url = add_template()
#         self.update_url = update_template()
#         self.send_url = get_template_send()
#         self.delete_url = delete_template()
#         super(SendCloudTemplate, self).__init__(*args, **kwargs)
#
#     @property
#     def edm_user(self):
#         return self._edm_user
#
#     def get_or_create(self, **kwargs):
#         if not self.get_status():
#             self.add(**kwargs)
#
#     def update_or_create(self, **kwargs):
#         if not self.get_status():
#             self.add(**kwargs)
#         else:
#             self.update(**kwargs)
#
#     def get_status(self):
#         data = {
#             'apiUser': self.api_user,
#             'apiKey': self.api_key,
#             'invokeName': self.invoke_name
#         }
#
#         try:
#             res = self.post_api(self.get_url, data)
#             return True
#         except SendCloudAPIError as e:
#             return False
#         # if res['statusCode'] == 40216:
#         #     return res['result']
#         # else:
#         #     return res['result']
#
#     def add(self, name, html, subject, email_type=1):
#         data = {
#             'apiUser': self.api_user,
#             'apiKey': self.api_key,
#             'invokeName': self.invoke_name,
#             'name': name,
#             'html': html,
#             'subject': subject,
#             'templateType': email_type
#         }
#         return self.post_api(self.add_url, data)
#
#     def update(self, name, html, subject, email_type=1):
#         data = {
#             'apiUser': self.api_user,
#             'apiKey': self.api_key,
#             'invokeName': self.invoke_name,
#             'name': name,
#             'html': html,
#             'subject': subject,
#             'templateType': email_type
#         }
#         return self.post_api(self.update_url, data)
#
#     def delete(self):
#         data = {
#             'apiUser': self.api_user,
#             'apiKey': self.api_key,
#             'invokeName': self.invoke_name,
#         }
#         res = self.post_api(self.delete_url, data)
#         return res
#
#     def send_to_list(self, subject, from_mail, from_name, to):
#         data = {
#             'apiUser': self.edm_user,
#             'apiKey': self.api_key,
#             'useAddressList': 'true',
#             'respEmailId': 'true',
#             'templateInvokeName': self.invoke_name,
#             'subject': subject,
#             'to': to,
#             "from": from_mail,
#             "fromName": from_name,
#         }
#         return self.post_api(self.send_url, data)


from .base import SendCloudAPIBase
from .conf import (
    get_template_list,
    update_template,
    add_template,
    delete_template,
    get_template,
)


class TemplateAPI(SendCloudAPIBase):

    def __init__(self, invoke_name=None):
        self._invoke_name = invoke_name

    @property
    def invoke_name(self):
        return self._invoke_name

    @property
    def list_template_url(self):
        return get_template_list()

    @property
    def get_template_url(self):
        return get_template()

    @property
    def add_template_url(self):
        return add_template()

    @property
    def update_template_url(self):
        return update_template()

    @property
    def delete_template_url(self):
        return delete_template()

    def list(self, template_type=1, star=0, limit=100):
        # _data = self.get_payload()

        _data = {
            "templateType": template_type,
            "start": star,
            "limit": limit,
        }

        if self.invoke_name:
            _data.update(
                {
                    "invoke_name": self.invoke_name,
                })

        r = self.post(self.list_template_url, **_data)
        return r
