
#Token:令牌，需要账号密码验证获取token值
# body:
#    data:表单格式   data=
#    json:json格式   json=   请求头默认为application/json


# 1、获取token值
import requests
token_url = 'https://www.csdn.net/community/toolbar-api/v1/get-user-info'  # url
payLoad = {"userName": "j201903070064", "password": "362387359"}  # 请求体
head_token = {"Content-Type": 'application/json'}  # 请求头

#发送请求
resp=requests.post(token_url,json=payLoad)
print(resp.json())
# 2、新增用户接口


#python生成随机数
# import random
# print(f'123{random.randint(11111,99999)}')


'''
    优化：
    1-封装
    2-结合测试用例
    3-结合pytest框架
    4-导出allure报告
    5-优化报告
    6-调试
    7-jenkins
    8-邮件通知
'''