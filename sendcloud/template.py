import logging

from .base import SendCloudAPIBase
from .conf import (
    get_template_list,
    update_template,
    add_template,
    delete_template,
    get_template,
)

logger = logging.getLogger("sendcloud")


class TemplateAPI(SendCloudAPIBase):
    def __init__(self, invoke_name=None):
        self._invoke_name = invoke_name

    @property
    def invoke_name(self):
        return self._invoke_name

    @property
    def list_template_url(self):
        return get_template_list()

    @property
    def get_template_url(self):
        return get_template()

    @property
    def add_template_url(self):
        return add_template()

    @property
    def update_template_url(self):
        return update_template()

    @property
    def delete_template_url(self):
        return delete_template()

    def list(self, template_type=1, start=0, limit=30):
        _data = {"templateType": template_type, "start": start, "limit": limit}
        if self.invoke_name:
            _data.update({"invoke_name": self.invoke_name})
        r = self.post(self.list_template_url, **_data)
        return r

    def get(self):
        if self.invoke_name is None:
            raise ValueError("The given invoke name have must be set")
        _data = {"invoke_name": self.invoke_name}
        r = self.post(url=self.get_template_url, **_data)
        logger.info(r)
        return r

    def add(self, name, html, subject, email_type=1):
        """

        :param name: 邮件模板名称
        :param html: html格式内容
        :param subject: 模板标题
        :param email_type: 邮件模板类型: 0(触发), 1(批量)
        :return: {
                    "statusCode": 200,
                    "info": {
                        "data": {
                            "name": "test",
                            "invokeName": "testtemplate",
                            "templateType": 0,
                            "gmtCreated": "2015-10-16 10:42:01",
                            "gmtUpdated": "",
                            "html": "<p>add new template</p>",
                            "subject": "test_subject"
                        }
                    },
                    "message": "请求成功",
                    "result": true
                }
        """

        if name is None:
            raise ValueError("The given name have must be set")
        if html is None:
            raise ValueError("The given html have must be set")
        if subject is None:
            raise ValueError("The given subject have must be set")

        _data = {
            "name": name,
            "html": html,
            "subject": subject,
            "templateType": email_type,
        }

        if self.invoke_name:
            _data.update({"invoke_name": self.invoke_name})

        r = self.post(url=self.add_template_url, **_data)
        logger.info(r)
        return r

    def delete(self):
        if self.invoke_name is None:
            raise ValueError("The given invoke name have must be set")
        _data = {"invoke_name": self.invoke_name}
        r = self.post(url=self.delete_template_url, **_data)
        logger.info(r)
        return r

    def update(self, name, html, subject, email_type=1):
        _data = {"templateType": email_type}
        if name is not None:
            _data.update({"name": name})
        if html is not None:
            _data.update({"html": html})
        if subject is not None:
            _data.update({"subject": subject})

        if self.invoke_name:
            _data.update({"invoke_name": self.invoke_name})
        r = self.post(url=self.update_template_url, **_data)
        logger.info(r)
        return r
