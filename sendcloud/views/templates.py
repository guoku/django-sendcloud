import logging
from django.views import generic
from sendcloud.core import TemplateAPI
from sendcloud.core.paginator import Paginator

logger = logging.getLogger('sendcloud')


class MailTemplateListView(generic.ListView):
    template_name = "sendcloud/template/list.html"
    paginator_class = Paginator
    paginate_by = 30

    @property
    def page_start(self):
        try:
            _page = int(self.request.GET.get(self.page_kwarg, 1))
            _start = (_page - 1) * self.paginate_by
        except (TypeError, ValueError):
            _start = 0
        return _start

    def get_queryset(self):
        t = TemplateAPI()
        r = t.list(start=self.page_start, limit=self.paginate_by)
        return r
