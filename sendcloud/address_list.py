import logging
from django.conf import settings
from sendcloud import APIBaseClass

from .conf import (
    member_list,
    member_update,
    member_get,
    member_add,
    member_delete,
)

logger = logging.getLogger('sendcloud')


class SendCloudAddressList(APIBaseClass):
    def __init__(self, fail_silently=False, *args, **kwargs):
        mail_list_addr, member_addr = (kwargs.pop('mail_list_addr', None),
                                       kwargs.pop('member_addr', None))
        try:
            self._mail_list_addr = mail_list_addr or getattr(settings,
                                                             'MAIL_LIST')
        except AttributeError:
            if fail_silently:
                self._mail_list_addr = None
            else:
                raise

        self._member_addr = member_addr
        self.fail_silently = fail_silently
        # self.add_member_url = 'http://sendcloud.sohu.com/webapi/list_member.add.json'
        # self.update_member_url = 'http://sendcloud.sohu.com/webapi/list_member.update.json'
        # self.delete_member_url = 'http://sendcloud.sohu.com/webapi/list_member.delete.json'
        # self.get_member_url = 'http://sendcloud.sohu.com/webapi/list_member.get.json'
        # self.get_list_url = 'http://sendcloud.sohu.com/webapi/list.get.json'
        self.create_list_url = 'http://sendcloud.sohu.com/webapi/list.create.json'

        self.get_list_url = member_list()
        self.add_member_url = member_add()
        self.update_member_url = member_update()
        self.delete_member_url = member_delete()
        self.get_member_url = member_get()

        super(SendCloudAddressList, self).__init__(*args, **kwargs)

    @property
    def mail_list_addr(self):
        return self._mail_list_addr

    @property
    def member_addr(self):
        return self._member_addr

    def create_list(self, list_name):
        data = {
            'api_user': self.api_user,
            'api_key': self.api_key,
            'mail_list_addr': list_name,
            'member_addr': self.member_addr,
        }
        return self.post_api(self.create_list_url, data)

    def get_list(self, start=0, limit=100):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'address': self.mail_list_addr,
            'start': start,
            'limit': limit,
        }
        res = self.post_api(self.get_list_url, data)
        logger.info(res)
        return res['info']

    def get_or_create(self, name):
        member = self.get()
        if member:
            return member
        return self.add_member(name)

    def get(self):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'address': self.mail_list_addr,
            'members': self.member_addr,
        }
        res = self.post_api(self.get_member_url, data)
        logger.info(res)
        return res["info"]

    def add_member(self, names=None, vars={}):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'address': self.mail_list_addr,
            'members': self.member_addr,
            # 'vars': vars,
        }
        if names:
            data.update({
                "names": names
            })
        return self.post_api(self.add_member_url, data)

    def update_member(self, name='', member_addr='', mai_list_addr='', vars=''):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'address': mai_list_addr or self.mail_list_addr,
            'members': member_addr or self.member_addr,
        }
        if name:
            data['names'] = name
        # if member_addr:
        #     data['member_addr'] = member_addr
        if vars:
            data[vars] = vars
        return self.post_api(self.update_member_url, data)

    def delete_member(self):
        data = {
            'apiUser': self.api_user,
            'apiKey': self.api_key,
            'address': self.mail_list_addr,
            'members': self.member_addr,
        }
        return self.post_api(self.delete_member_url, data)
