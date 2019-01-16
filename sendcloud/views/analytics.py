import logging
from django.views import generic
from sendcloud.core.analytics import AnalyticsAPI

logger = logging.getLogger('sendcloud')


class InvalidStatView(generic.ListView):
    template_name = 'sendcloud/analytics/invalid_stat.html'

    def get_queryset(self):
        a = AnalyticsAPI().invalid_stat()
        return a["info"]["dataList"]

    # def get_context_data(self, **kwargs):
    #     _context = super(InvalidStatView, self).get_context_data(**kwargs)
    #
    #     _invalid_stat = self.get_invalid_stat()
    #     logger.info(_invalid_stat)
    #
    #     return _context
