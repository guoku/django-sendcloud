from django.conf.urls import url
from .views import MailTemplateListView
from .views.dashboard import DashboardView


urlpatterns = [

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
    url(r'^template/$', MailTemplateListView.as_view()),

]
