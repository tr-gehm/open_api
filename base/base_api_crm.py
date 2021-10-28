# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: base_api_crm.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
"""
import time
from requests import request
from common.handle_config import conf
from common.handle_openapi import HandleOpenapi
from jsonpath import jsonpath
from common.handle_request import HandleRequest

expires = conf.get("env", "expires")
headers = eval(conf.get("env", "headers"))


class CrmBaseApi:

    @staticmethod
    def create_customer():
        """创建客户资料"""
        # 请求地址
        api = HandleOpenapi(path="create_customer", method="POST")
        url = api.sign()
        name = "customer" + str(time.time())
        data = {
            "name": name,
            "tel": [HandleRequest.random_phone()],
            "level": 0,
            "shareType": 0,
            "share": None,
            "sex": 0,
            "email": "zhangsan@xxx.com.cn",
            "remark": None,
            "address": "河北省沧州市"
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)
        res = response.json()
        customer_id = jsonpath(res, "$..id")[0]
        return customer_id

    @staticmethod
    def delete_customer(customer_id):
        """删除客户资料"""
        # 请求地址
        api = HandleOpenapi(path="delete_customer", method="POST")
        url = api.sign()
        name = "customer" + str(time.time())
        data = {
            "id": customer_id
        }
        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)
        res = response.json()
        customer_id = jsonpath(res, "$..id")[0]
        return customer_id
