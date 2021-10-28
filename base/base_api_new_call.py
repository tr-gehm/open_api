# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/25 15:14
@Auth ： ghm
@File ：base_api_new_call.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import time
from requests import request
from common.handle_openapi import HandleOpenapi
from common.handle_request import HandleRequest
from common.config import *

expires = config.get("env", "expires")
headers = eval(config.get("env", "headers"))


class CallBaseApi:

    @staticmethod
    def online():
        """座席上线"""
        # 请求地址
        api = HandleOpenapi(path="online", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("call_sdk", "cno"),
            "bindTel": config.get("call_sdk", "tel"),
            "bindType": 1,
            "status": 1
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def offline():
        """座席下线"""
        api = HandleOpenapi(path="offline", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("call_sdk", "cno"),
            "unbindTel": 0
        }
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def pause():
        """座席置忙"""
        api = HandleOpenapi(path="pause", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("call_sdk", "cno"),
            "description": "忙碌"
        }
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def unpause():
        """座席置闲"""
        api = HandleOpenapi(path="unpause", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("call_sdk", "cno")
        }
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def create_client():
        """新增座席"""
        api = HandleOpenapi(path="create_client", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("clink2_setting", "setting_cno"),
            "name": "新增座席01",
            "areaCode": "010",
            "password": "Aa123456",
            "role": 1,
            "active": 1,
            "qnos": [
                "0000"
            ],
            "hiddenTel": 1,
            "permission": {
                "asr": 0,
                "call": 1,
                "cdr": 1,
                "recordDownload": 1,
                "sms": 1,
                "record": 3,
                "chat": 0
            },
            "type": 1,
            "chatLimit": 1,
            "chatLimitNum": 1
        }
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def delete_client():
        """删除座席"""
        api = HandleOpenapi(path="delete_client", method="POST")
        url = api.sign()
        data = {
            "cno": config.get("clink2_setting", "setting_cno")
        }

        response = request(method="POST", url=url, json=data, headers=headers)
