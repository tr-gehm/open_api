# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_chat_message_to_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
chat_message_to_client:访客给座席发送消息
appId对应的导航：北京平台“高杰SDK测试”
"""

import os
import time
import unittest
from common.handle_data import EnvData
from unittestreport import rerun
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from common.handle_path import DATA_DIR
from base.base_api_im import ImBaseApi
from common.handle_request import HandleRequest

sheet_name = "chat_message_to_client"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class ChatMessageToClientTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        ImBaseApi.cno_login()
        cls.session_id = ImBaseApi.visitor_open_session()

    @data(*cases)
    @rerun(count=3, interval=2)
    def test_chat_message_to_client(self, case):
        # 第一步：准备用例数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        case["data"] = case["data"].replace("#sessionId#", self.session_id)

        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)

        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    @classmethod
    def tearDownClass(cls):
        # 座席关闭会话
        ImBaseApi.client_close_session(session_id=cls.session_id)
        ImBaseApi.cno_logout()
