# Requests

是Python HTTP的库

安装命令：pip install requests

https://requests.readthedocs.io/zh_CN/latest/

## 接口测试实例

**对自己聊天室项目的登陆及获取频道列表的简单测试**

### 测试登陆接口

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201022220905066.png" alt="image-20201022220905066" style="zoom:67%;" />

```python
def login():
    url = 'http://39.98.227.201:8080/chatroom/login'

    data = {
        'name': 'mumu',
        'password': '123456'
    }
    data_json = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(url=url, headers=headers, data=data_json)
    print(r.cookies)
    print(r.text)
```

## 获取频道列表

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20201022221027426.png" alt="image-20201022221027426" style="zoom:67%;" />

**注意啦！,获取频道列表需要保持登陆状态**

- 第一种方式：先运行登录接口，然后从loginRes中获取cookies

```python
def getChannel():
    url = 'http://39.98.227.201:8080/chatroom/channel'
    # 先运行登录接口，然后从loginRes中获取cookies
    cookies = {
        'JSESSIONID': '22F9F124B120C1E986C1CE0029F0A7F0'
    }
    r = requests.get(url=url, params=None, cookies=cookies)
    print(r.text)

```



- 第二种方式：使用会话对象保持登录，也就是使用Session

```python\
def getChannels1():
    # 使用会话对象保持登录
    url1 = 'http://39.98.227.201:8080/chatroom/login'

    data = {
        'name': 'mumu',
        'password': '123456'
    }
    data_json = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    url2 = 'http://39.98.227.201:8080/chatroom/channel'
    sessionRequests = requests.session()
    resp = sessionRequests.post(url=url1, headers=headers, data=data_json)
    r = sessionRequests.get(url=url2, params=None)
    print(r.text)
```

