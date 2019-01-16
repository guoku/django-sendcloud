from .base import SendCloudAPIBase
from ..conf import get_invalid_stat_url


class AnalyticsAPI(SendCloudAPIBase):

    @property
    def invalid_stat_url(self):
        return get_invalid_stat_url()

    def invalid_stat(self):
        data = {
            "days": 3,
        }
        r = self.post(self.invalid_stat_url, **data)

        return r
