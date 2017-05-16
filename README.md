# account_server

在大规模抓取的时候需要大量账号的支持，为了方便管理做成了一个服务。

使用的框架是 Flask。现在已经完成了 mongo 实现，其他可以自行实现。

account_helper.py 是我封装的获取 account、新增 account 和删除 account 的函数，可以直接使用，还包含了生成用户名和密码的函数。


## 一、API

每个请求都需要加上token

### 1、获取accont

数据库层按照使用时间排序返回，最长时间没有被使用的账号将会被有限返回。


```
GET /select?site=site&count=count
```

##### Params 

| Name | Type | Description |
| ----| ---- | ---- |
| site | string | 网站名称|
| count | int | 数量 |

##### Response

```
{
    'status': 状态码 0: 成功 | 1: 失败
    'info': 状态信息 
    'data': data#实际请求的值
}
```
data 格式如下：

| Name | Type | Description |
| ----| ---- | ---- |
| uid | string | 用户uid，根据site和uname生成的md5，唯一标示用户 |
| site | string | 网站名 |
| uname | string | 用户名 |
| passwd | string | 密码 |
| cookie | json string | 可以为空 |
| email | string | 可以为空 |
| extra | string | 冗余信息，可以为空 |

##### demo

服务默认运行在本机的5002端口，请求1个socks5代理的请求如下：

```
http://127.0.0.1:5002/select?site=angel&count=1&token=
```

返回:

```
{
'status':0,
'info':'ok',
'data':{u'uid': u'49e979fee94b3***2a41555f948459', u'extra': None, u'passwd': u'X1214***013F', u'site': u'angel', u'uname': u'DLvec ****', u'cookie': u'{"_angellist": "bfba51e***68b15a374f329", "visitor_hash": "29182c95513e364c***db5c7"}', u'email': None}
}

```

## 2、删除account

数据库层是通过uid删除对应的proxy。

```
GET /delete?uid=uid
```

##### Params 

| Name | Type | Description |
| ----| ---- | ---- |
| uid | string | 用户uid，根据site和uname生成的md5，唯一标示用户 |

##### Response

```
{
    'status': 状态码 0: 成功 | 1: 失败
    'info': 状态信息 
}
```

##### demo

服务默认运行在本机的5002端口，请求1个socks5代理的请求如下：

```
http://127.0.0.1:5002/delete?uid=49e979fee94b3***2a41555f948459
```

返回:

```
{
'status':0,
'info':'ok',
}

```

## 3、新增account

插入新的account。

```
GET /insert?site=site&uname=uname&passwd=passwd&cookie=cookie&email=email&extra=extra
```

##### Params 

| Name | Type | Description |
| ----| ---- | ---- |
| site | string | 网站名 |
| uname | string | 用户名 |
| passwd | string | 密码 |
| cookie | json string | 可以为空 |
| email | string | 可以为空 |
| extra | string | 冗余信息，可以为空 |

##### Response

```
{
    'status': 状态码 0: 成功 | 1: 失败
    'info': 状态信息 
}
```

##### demo

服务默认运行在本机的5002端口，请求1个socks5代理的请求如下：

```
http://127.0.0.1:5002/delete?site=angelsite=angel&site=angel&uname=adasddwqwq&passwd=dsadawdw```

返回:

```
{
'status':0,
'info':'ok',
}

```

