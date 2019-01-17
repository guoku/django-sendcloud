from django.conf.urls import url
from .views import MailTemplateListView
from .views.dashboard import DashboardView
from .views.analytics import InvalidStatView


urlpatterns = [

    url(r'^dashboard/$', DashboardView.as_view(), name='send_cloud_dashboard'),

    url(r'^template/$', MailTemplateListView.as_view(), name='send_cloud_template_list'),


    url(r'^analytics/invalid/$', InvalidStatView.as_view(), name='send_cloud_invalid_stat'),

]
