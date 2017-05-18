# account_server

在大规模抓取的时候需要大量账号的支持，为了方便管理做成了一个服务。

使用的框架是 Flask。现在已经完成了 mongodb 实现，其他数据库可以自行实现。

account_helper.py 是我封装的获取 account、新增 account 和删除 account 的函数，可以直接使用，还包含了生成用户名和密码的函数。


## 一、API

最近发现了一个很好用的API管理网站[eolinker](https://www.eolinker.com)，界面好看、功能好用，还开源，强烈推荐一下。

本项目的接口已经移到了上面，访问地址是: [account_server API in echolinker](https://sp.eolinker.com/LGbtdj) 。 
