import logging
from django.views import generic
from sendcloud.core.members import MemberAPI

logger = logging.getLogger('django')


class MemberListView(generic.ListView):
    template_name = 'sendcloud/members/list.html'

    def get_queryset(self):
        members = MemberAPI().list(address=self.request.GET.get('address', None))
        logger.info(members)
        return members



class MemberDeleteView(generic.DeleteView):
    template_name = 'sendcloud/members/delete.html'
    pass
