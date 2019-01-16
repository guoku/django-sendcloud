import logging
import requests
from ..exceptions import SendCloudAPIError
from ..conf import (
    get_send_cloud_batch_user,
    get_send_cloud_batch_key,
)

logger = logging.getLogger('sendcloud')


class SendCloudAPIBase(object):

    def __init__(self):
        pass

    @property
    def app_user(self):
        return get_send_cloud_batch_user()

    @property
    def app_key(self):
        return get_send_cloud_batch_key()

    def get_payload(self):
        _data = {
            "apiUser": self.app_user,
            "apiKey": self.app_key
        }
        return _data

    def get(self, url, **kwargs):
        payload = self.get_payload()
        payload.update(**kwargs)
        logger.info(payload)
        r = requests.get(url=url, params=payload)
        logger.info(r.content)
        if r.status_code == 200:
            return r.json()
        else:
            raise SendCloudAPIError(r.text)

    def post(self, url, **kwargs):
        payload = self.get_payload()
        payload.update(**kwargs)
        logger.info(payload)
        r = requests.post(url=url, data=payload)
        logger.info(r.content)
        if r.status_code == 200:
            return r.json()
        else:
            raise SendCloudAPIError(r.text)
