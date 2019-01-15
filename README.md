## Django SendCloud


[![GitHub license](https://img.shields.io/github/license/edison7500/django-sendcloud.svg)](https://github.com/edison7500/django-sendcloud/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/edison7500/django-sendcloud.svg)](https://github.com/edison7500/django-sendcloud/issues)
[![GitHub forks](https://img.shields.io/github/forks/edison7500/django-sendcloud.svg)](https://github.com/edison7500/django-sendcloud/network)
[![GitHub stars](https://img.shields.io/github/stars/edison7500/django-sendcloud.svg)](https://github.com/edison7500/django-sendcloud/stargazers)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/edison7500/django-sendcloud.svg?style=social)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fedison7500%2Fdjango-sendcloud)


send cloud django 插件

> 本人已经离开果库。因此，本项目 fork 到我自己的 github 仓库进行维护。


## Overview

**Install** 

```.bash
python setup.py install
```

**在 Django 的 settings.py 加入** 

```.python

# mail config
EMAIL_BACKEND = 'sendcloud.backend.SendCloudBackend'
DEFAULT_FROM_EMAIL = "noreply@example.com"

SEND_CLOUD_KEY = {
    "spark_key": {
        "APP_USER": "replace_me",
        "APP_KEY": "replace_me",
    },
    "batch_key": {
        "APP_USER": "replace_me",
        "APP_KEY": "replace_me",
    }
}

```



