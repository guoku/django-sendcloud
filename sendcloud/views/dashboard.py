import logging
from django.views import generic
from sendcloud.core.user_info import UserInfoAPI

logger = logging.getLogger('sendcloud')


class DashboardView(generic.TemplateView):
    template_name = 'sendcloud/template/dashboard.html'

    def get_userinfo(self):
        r = UserInfoAPI().user_info()
        return r['info']

    def get_context_data(self, **kwargs):
        _context = super(DashboardView, self).get_context_data()
        _userinfo = self.get_userinfo()
        logger.info(_userinfo)
        _context.update(_userinfo)
        return _context
