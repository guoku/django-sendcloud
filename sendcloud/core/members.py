import logging
from .base import SendCloudAPIBase
from ..conf import (
    member_list,
    member_get,
    member_delete,
    member_update,
    member_add,
)

logger = logging.getLogger('django')


class MemberAPI(SendCloudAPIBase):
    #
    # _star = 0
    # _limit = 100
    _total = 0
    _count = 0

    @property
    def member_list_url(self):
        return member_list()

    @property
    def member_get_url(self):
        return member_get()

    @property
    def member_add_url(self):
        return member_add()

    @property
    def member_update_url(self):
        return member_update()

    @property
    def member_delete_url(self):
        return member_delete()

    @property
    def total(self):
        return self.validate_number(self._total)

    @property
    def count(self):
        return self.validate_number(self._count)

    def list(self, address=None, star=0, limit=100):
        if address is None:
            raise ValueError("The given address have must be set!")
        _data = {
            "address": address,
            'star': star,
            'limit': limit,
        }
        r = self.post(url=self.member_list_url, **_data)
        # logger.info(r)

        self._count = r['info']['count']
        self._total = r['info']['total']

        return r['info']['dataList']

    def add(self, address=None, members=[]):
        if address is None:
            raise ValueError("The given address have must be set!")
        _data = {
            "address": address,
            "members": ';'.join(members),
        }

        r = self.post(url=self.member_add_url, **_data)

        return r['info']

    def update(self, address=None, members=[], new_members=[]):
        if address is None:
            raise ValueError("The given address have must be set!")

        _data = {
            "address": address,
            "members": ';'.join(members),
            "newMembers": ';'.join(new_members),
        }
        r = self.post(url=self.member_update_url, **_data)
        return r['info']

    def delete(self, address=None, members=[]):
        if address is None:
            raise ValueError("The given address have must be set!")

        _data = {
            "address": address,
            "members": ';'.join(members),
        }
        r = self.post(url=self.member_delete_url, **_data)

        return r['info']
