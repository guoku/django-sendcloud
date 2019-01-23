import logging

from django.urls import reverse, reverse_lazy
from django.views import generic
from sendcloud.core.address_list import AddressListAPI
from sendcloud.forms.address import AddressListForm

logger = logging.getLogger('django')


class AddressListView(generic.ListView):
    template_name = "sendcloud/address/list.html"

    def get_queryset(self):
        ad = AddressListAPI()
        r = ad.list()
        return r["info"]["dataList"]


class AddressCreateView(generic.CreateView):
    template_name = "sendcloud/address/add.html"
    form_class = AddressListForm
    success_url = reverse_lazy('send_cloud_address_list')
