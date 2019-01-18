from django import forms


class AddressListForm(forms.Form):
    address = forms.EmailField()
    name = forms.CharField()
    desc = forms.CharField(required=False)
