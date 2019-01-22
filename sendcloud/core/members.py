from .base import SendCloudAPIBase
from ..conf import (
    member_list,
    member_get,
    member_delete,
    member_update,
    member_add,
)


class MemberAPI(SendCloudAPIBase):

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

    def list(self, address=None, star=0, limit=100):
        _data = {
            'star': star,
            'limit': limit,
        }
        #     "address": address
        # }
        if address is not None:
            _data = {
                "address": address
            }

        r = self.post(url=self.member_get_url, **_data)
