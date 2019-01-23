# import logging
# from django.views import generic
# from ..template import TemplateAPI
#
# logger = logging.getLogger('sendcloud')
#
#
# class MailTemplateListView(generic.ListView):
#     template_name = "sendcloud/template/list.html"
#
#     def get_queryset(self):
#         t = TemplateAPI()
#         r = t.list()
#         # logger.info(r)
#         return r['info']['dataList']

from .templates import MailTemplateListView
from .members import MemberListView
from .address import (
    AddressListView,
    AddressCreateView,
)

__all__ = [
    'MailTemplateListView',
    'AddressListView',
    'AddressCreateView',
    'MemberListView',
]
