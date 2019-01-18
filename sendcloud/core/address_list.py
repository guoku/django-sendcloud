import logging
from .base import SendCloudAPIBase
from ..conf import (
    address_list,
    address_add,
    address_update,
    address_delete,
)

logger = logging.getLogger('django')


class AddressListAPI(SendCloudAPIBase):
    #
    # def __init__(self):
    #     pass

    @property
    def address_list_url(self):
        return address_list()

    @property
    def address_add_url(self):
        return address_add()

    @property
    def address_update_url(self):
        return address_update()

    @property
    def address_delete_url(self):
        return address_delete()

    def list(self, address=[], star=0, limit=100):
        _data = {
            "star": star,
            "limit": limit,
        }

        if len(address) > 1:
            address_string = ";".join(address)
            _data.update({
                "address": address_string,
            })

        r = self.post(url=self.address_list_url, **_data)
        logger.info(r)

        return r

    def add(self, **kwargs):
        kwargs.setdefault('listType', 0)

        _address = kwargs.pop('address', None)
        _name = kwargs.pop('name', None)
        _desc = kwargs.pop('desc', None)

        if _address is None:
            raise ValueError("The given address have must be set")
        if _name is None:
            raise ValueError("The given name have must be set")

        _data = {
            "address": _address,
            "name": _name,
            "listType": kwargs.get('listType')
        }

        if _desc is not None:
            _data.update({
                "desc": _desc,
            })

        r = self.post(url=self.address_add_url, **_data)
        logger.info(r)
        return r
