from django.conf.urls import url

from sendcloud.views import (
    AddressListView,
    AddressCreateView,
    MemberListView,
    MailTemplateListView
)
# from .views import MailTemplateListView
from .views.dashboard import DashboardView
from .views.analytics import InvalidStatView
# from .views.address import (
#     AddressListView,
#     AddressCreateView
# )
from .views.api_user import APIUserListView


urlpatterns = [

    url(r'^dashboard/$', DashboardView.as_view(), name='send_cloud_dashboard'),

    url(r'^template/$', MailTemplateListView.as_view(), name='send_cloud_template_list'),

    url(r'^address/$', AddressListView.as_view(), name='send_cloud_address_list'),
    url(r'^address/add/?$', AddressCreateView.as_view(), name='send_cloud_address_add'),

    url(r'^members/$', MemberListView.as_view(), name='member_list'),


    url(r'^analytics/invalid/$', InvalidStatView.as_view(), name='send_cloud_invalid_stat'),

    url(r'^api/users/$', APIUserListView.as_view(), name='send_cloud_api_user'),
]
