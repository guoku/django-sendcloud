from django.views import generic
from sendcloud.core.user_info import UserInfoAPI


class APIUserListView(generic.ListView):
    template_name = "sendcloud/api_user/list.html"

    def get_queryset(self):
        u = UserInfoAPI().api_user_list()
        return u['info']['dataList']
