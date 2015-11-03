#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

from sendcloud import APIBaseClass


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
        self.add_url = 'http://sendcloud.sohu.com/webapi/list_member.add.json'
        self.update_url = 'http://sendcloud.sohu.com/webapi/list_member.update.json'
        self.delete_url = 'http://sendcloud.sohu.com/webapi/list_member.delete.json'
        self.get_url = 'http://sendcloud.sohu.com/webapi/list_member.get.json'
        super(SendCloudAddressList, self).__init__(*args, **kwargs)

    @property
    def mail_list_addr(self):
        return self._mail_list_addr

    @property
    def member_addr(self):
        return self._member_addr

    def get_or_create(self, name):
        member = self.get()
        if member:
            return member
        return self.add_member(name)

    def get(self):
        data = {
            'api_user': self.api_user,
            'api_key': self.api_key,
            'mail_list_addr': self.mail_list_addr,
            'member_addr': self.member_addr,
        }
        res = self.post_api(self.get_url, data)
        if res['members']:
            return res
        return res

    def add_member(self, name, vars='', upsert='false'):
        data = {
            'api_user': self.api_user,
            'api_key': self.api_key,
            'mail_list_addr': self.mail_list_addr,
            'member_addr': self.member_addr,
            'name': name,
            'vars': vars,
            'upsert': upsert
        }
        return self.post_api(self.add_url, data)

    def update_member(self, name='', member_addr='', mai_list_addr='', vars=''):
        data = {
            'api_user': self.api_user,
            'api_key': self.api_key,
            'mail_list_addr': mai_list_addr or self.mail_list_addr,
            'member_addr': member_addr or self.member_addr,
        }
        if name:
            data['name'] = name
        if vars:
            data[vars] = vars
        return self.post_api(self.update_url, data)

    def delete_member(self):
        data = {
            'api_user': self.api_user,
            'api_key': self.api_key,
            'mail_list_addr': self.mail_list_addr,
            'member_addr': self.member_addr,
        }
        return self.post_api(self.delete_url, data)
