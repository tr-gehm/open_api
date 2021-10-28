# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: base_api_im.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
"""
# from numpy import long
from requests import request
from common.handle_config import conf
from common.handle_openapi import HandleOpenapi
from jsonpath import jsonpath
from common.handle_data import EnvData

expires = conf.get("env", "expires")
headers = eval(conf.get("env", "headers"))


class ImBaseApi:
    @staticmethod
    def cno_login():
        """座席登录，状态空闲"""
        # 第一步：准备用例数据
        # 请求地址
        api = HandleOpenapi(path="chat_client_login", method="POST")
        url = api.sign()
        data = {
            "cno": conf.get("im_sdk", "cno"),
            "chatLimitNumber": int(conf.get("im_sdk", "chatLimitNumber")),
            "chatLoginStatus": 1
        }
        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def cno_logout():
        api = HandleOpenapi(path="chat_client_logout", method="POST")
        url = api.sign()
        data = {
            "cno": conf.get("im_sdk", "cno")
        }
        # 发送请求，获取结果
        response = request(method="POST", url=url, json=data, headers=headers)

    @staticmethod
    def visitor_close_session(session_id):
        """
        关闭会话
        """
        # 第一步：准备用例数据
        method = "POST"
        # 请求地址
        api = HandleOpenapi(path="chat_visitor_close_session", method=method)
        url = api.sign()
        data = {
            "sessionId": session_id
        }

        # 第二步：发送请求获取实际结果
        response = request(method=method, url=url, json=data, headers=headers)

    @staticmethod
    def visitor_open_session():
        """
        访客发起会话,无机器人
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_visitor_open_session", method="POST")
        url = api.sign()
        data = {
            "appId": conf.get("im_sdk", "appId")
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)
        res = response.json()
        session_id = jsonpath(res, "$..sessionId")[0]
        # start_time = jsonpath(res, "$..startTime")
        return session_id

    @staticmethod
    def visitor_open_robot_session():
        """
        访客发起会话，需要通过机器人
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_visitor_open_session", method="POST")
        url = api.sign()
        data = {
            "appId": conf.get("im_sdk", "robotAppId")
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers)
        res = response.json()
        session_id = jsonpath(res, "$..sessionId")[0]
        return session_id

    @staticmethod
    def client_chat_message_to_visitor(session_id):
        """
        座席发送消息给访客
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_message_to_visitor", method="POST")
        url = api.sign()
        data = {
            "cno": conf.get("im_sdk", "cno"),
            "senderType": 1,
            "sessionId": session_id,
            "messageType": 1,
            "content": "发送消息给访客"
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers, timeout=10)

    @staticmethod
    def client_close_session(session_id):
        """
        座席发送消息给访客
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_client_close_session", method="POST")
        url = api.sign()
        data = {
            "sessionId": session_id,
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers, timeout=10)

    @staticmethod
    def client_investigation(session_id):
        """
        座席发起满意度评价
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_client_investigation", method="POST")
        url = api.sign()
        data = {
            "cno": conf.get("im_sdk", "cno"),
            "sessionId": session_id
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers, timeout=10)
        res = response.json()

    @staticmethod
    def client_open_session():
        """
        座席主动发起会话
        :return: session_id
        """
        # 请求地址
        api = HandleOpenapi(path="chat_client_open_session", method="POST")
        url = api.sign()
        data = {
            "cno": conf.get("im_sdk", "cno"),
            "sessionId": getattr(EnvData, "session_id"),
            "startTime": getattr(EnvData, "session_start_time")
        }

        # 第二步：发送请求获取实际结果
        response = request(method="POST", url=url, json=data, headers=headers, timeout=10)

        res = response.json()


if __name__ == '__main__':
    ImBaseApi.visitor_open_session()
