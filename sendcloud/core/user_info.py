import logging
from .base import SendCloudAPIBase
from ..conf import (
    get_user_info_url, api_user_add_url, api_user_list_url)

logger = logging.getLogger('django')


class UserInfoAPI(SendCloudAPIBase):

    @property
    def user_info_url(self):
        return get_user_info_url()

    @property
    def api_user_list_url(self):
        return api_user_list_url()

    @property
    def api_user_add_url(self):
        return api_user_add_url()

    def user_info(self):
        r = self.post(url=self.user_info_url)
        logger.info(r)
        return r

    def api_user_list(self, **kwargs):
        """
            http://www.sendcloud.net/doc/email_v2/apiuser_do/
        :param kwargs: email_type, ctype, domain
        :return:
            {
                name: "***",
                cType: "非测试",
                emailType: "触发",
                domainName: "delong.com",
                neteaseSender: "",
                click: 1,
                open: 1,
                unsubscribe: 1
            }
        """
        _email_type = kwargs.pop('email_type', None)
        _ctype = kwargs.pop('ctype', None)
        _domain = kwargs.pop('domain', None)

        _data = dict()

        if _email_type:
            _data.update({
                "emailType": _email_type,
            })

        if _ctype:
            _data.update({
                "cType": _ctype,
            })

        if _domain:
            _data.update({
                "domainName": _domain,
            })

        r = self.post(url=self.api_user_list_url, **_data)
        logger.info(r)
        return r

    def api_user_add(self, domain=None, **kwargs):
        kwargs.setdefault('email_type', 0)
        kwargs.setdefault('ctype', 0)

        if domain is None:
            raise ValueError("The given domain must have set")

        _data = {
            "emailType": kwargs.get('email_type'),
            "cType": kwargs.get('ctype'),
            "domainName": domain,
        }

        r = self.post(url=self.api_user_add_url, **_data)
        logger.info(r)
        return r
