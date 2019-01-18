from .base import SendCloudAPIBase
from ..conf import (
    get_invalid_stat_url,
    get_task_info
)


class AnalyticsAPI(SendCloudAPIBase):

    @property
    def invalid_stat_url(self):
        return get_invalid_stat_url()

    @property
    def task_info_url(self):
        return get_task_info()

    def invalid_stat(self, days=3, **kwargs):
        _aggregate = kwargs.pop('aggregate', 0)
        data = {
            "days": days,
            "aggregate": _aggregate,
        }
        r = self.post(self.invalid_stat_url, **data)

        return r

    def task_info(self):

        pass