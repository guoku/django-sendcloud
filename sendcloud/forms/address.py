import logging
from django import forms
from sendcloud.core.address_list import AddressListAPI

logger = logging.getLogger('django')


class AddressListForm(forms.Form):
    address = forms.EmailField()
    name = forms.CharField()
    desc = forms.CharField(required=False)

    def __init__(self, instance=None, **kwargs):
        super(AddressListForm, self).__init__(**kwargs)

    def save(self):
        logger.info("======================")
        logger.info(self.cleaned_data)

        address_list = AddressListAPI()
        r = address_list.add(**self.cleaned_data)
        logger.info(r)
        return

        # address_list = AddressListAPI()
        # address_list.add()
