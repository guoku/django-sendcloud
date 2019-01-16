from django.conf.urls import url
from .views import MailTemplateListView
from .views.dashboard import DashboardView
from .views.analytics import InvalidStatView


urlpatterns = [

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^template/$', MailTemplateListView.as_view()),


    url(r'^analytics/invalid/$', InvalidStatView.as_view(), name='invalid_stat'),

]
