import logging
from .base import SendCloudAPIBase
from ..conf import get_user_info_url


logger = logging.getLogger('django')


class UserInfoAPI(SendCloudAPIBase):

    @property
    def user_info_url(self):
        return get_user_info_url()

    def user_info(self):
        r = self.post(url=self.user_info_url)
        logger.info(r)
        return r
