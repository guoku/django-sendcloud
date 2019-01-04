__version__ = '0.5.1'

import requests
import logging

# from django.conf import settings
from .settings import send_cloud_config
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address
from sendcloud.exceptions import SendCloudAPIError

# send_cloud_v2_send_api = "http://api.sendcloud.net/apiv2/mail/send"

logger = logging.getLogger("sendcloud")


class SendCloudBackend(BaseEmailBackend):
    """
        A Django Email backend that uses send cloud.
    """

    def __init__(self, fail_silently=False, *args, **kwargs):
        app_user, app_key = (kwargs.pop('app_user', None),
                             kwargs.pop('app_key', None))

        super(SendCloudBackend, self).__init__(fail_silently=fail_silently,
                                               *args, **kwargs)
        try:
            self._app_user = app_user or send_cloud_config.get('app_user')
            self._app_key = app_key or send_cloud_config.get('app_key')
        except KeyError:
            if fail_silently:
                self._app_user, self._app_key = None, None
            else:
                raise
        # self._api_url =

    @property
    def app_user(self):
        return self._app_user

    @property
    def app_key(self):
        return self._app_key

    @property
    def api_url(self):
        _api_url = send_cloud_config.get('send_mail')
        return _api_url

    def open(self):
        pass

    def close(self):
        pass

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        # print (dir(email_message))
        if not email_message.recipients():
            return False
        from_email = sanitize_address(email_message.from_email,
                                      email_message.encoding)
        # from_name = sanitize_address(email_message.from_name,
        #                              email_message.encoding)
        recipients = [sanitize_address(addr, email_message.encoding)
                      for addr in email_message.recipients()]

        params = {
            "apiUser": self.app_user,
            "apiKey": self.app_key,
            # "templateInvokeName": template,
            "subject": email_message.subject,
            "from": from_email,
            "to": recipients,
            "html": email_message.body,
        }

        r = requests.post(self.api_url, files={}, data=params)

        if r.status_code != 200:
            if not self.fail_silently:
                raise SendCloudAPIError(r.text)
            return False

        res = r.json()
        if not res['result']:
            logger.info(res['message'])
            raise SendCloudAPIError(res['message'])
        return True

    def send_messages(self, email_messages):
        """Sends one or more EmailMessage objects and returns the number of
        email messages sent.
        """
        if not email_messages:
            return

        num_sent = 0
        for message in email_messages:
            if self._send(message):
                num_sent += 1

        return num_sent


class APIBaseClass(object):
    def __init__(self, fail_silently=False, *args, **kwargs):
        api_user, api_key = (kwargs.pop('app_user', None),
                             kwargs.pop('app_key', None))
        self.fail_silently = fail_silently
        try:
            self._api_user = api_user or getattr(settings, 'MAIL_APP_USER')
            self._api_key = api_key or getattr(settings, 'MAIL_APP_KEY')
        except AttributeError:
            if fail_silently:
                self._api_user, self._api_key = None, None
            else:
                raise

    @property
    def api_user(self):
        return self._api_user

    @property
    def api_key(self):
        return self._api_key

    def post_api(self, url, data):
        try:
            r = requests.post(url, data=data)
        except Exception as e:
            logger.info(e)
            if not self.fail_silently:
                raise
            return False

        res = r.json()
        if not res['result']:
            raise SendCloudAPIError(res['message'])
        return True


__author__ = 'edison7500'
