from sendcloud.core import TemplateAPI, AnalyticsAPI


class TemplateListMixin(object):

    def get_template_list(self, start=0, size=3):
        _tl = TemplateAPI().list(start=start, limit=size)
        return _tl["info"]["dataList"]


class MailStatusMixin(object):
    def get_invalid_stat(self):
        _rs = AnalyticsAPI().invalid_stat(days=1)
        return _rs["info"]["dataList"]
