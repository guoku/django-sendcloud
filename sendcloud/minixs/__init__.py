from ..template import TemplateAPI


class TemplateListMixin(object):

    def get_template_list(self, start=0, size=3):
        _tl = TemplateAPI().list(start=0, limit=size)
        return _tl['info']['dataList']
