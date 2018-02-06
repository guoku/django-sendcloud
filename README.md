## Django SendCloud
send cloud django 插件

> 本人已经离开果库。因此，本项目 fork 到我自己的 github 仓库进行维护。


## Overview

**Install** 

```.bash
python setup.py install
```

**在 Django 的 settings.py 加入** 

```.python

EMAIL_BACKEND = 'sendcloud.SendCloudBackend'
MAIL_APP_USER = '***' # 使用api_user 和 api_key 进行验证    
MAIL_APP_KEY = '***'

```



