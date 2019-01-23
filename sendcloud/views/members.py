from django.views import generic
from sendcloud.core.members import MemberAPI


class MemberListView(generic.ListView):
    template_name = 'sendcloud/members/list.html'

    def get_queryset(self):

        members = MemberAPI().list(address=self.request.GET.get('address', None))

        return members