from django.conf.urls import url
from .views import MailTemplateListView


urlpatterns = [

    url(r'^template/$', MailTemplateListView.as_view())

]
