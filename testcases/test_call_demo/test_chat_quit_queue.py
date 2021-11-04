# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_chat_quit_queue.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
chat_quit_queue:访客退出排队
"""

import os
import time
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DATA_DIR
from common.handle_config import conf
from base.base_api_im import ImBaseApi

sheet_name = "chat_quit_queue"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class ChatQuitQueueTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        ImBaseApi.cno_login()
        time.sleep(3)

    def setUp(self):
        """
        发起会话，为访客主动关闭会话做准备
        :return:
        """
        number = int(conf.get("im_sdk", "chatLimitNumber"))
        self.sessions = []
        i = 0
        while i < (number + 1):
            self.session_id = ImBaseApi.visitor_open_session()
            self.sessions.append(self.session_id)
            i += 1
        time.sleep(3)
        # print("sessions:", self.sessions)

    @data(*cases)
    def test_chat_quit_queue(self, case):
        # 第一步：准备用例数据
        case["data"] = case["data"].replace("#sessionId#", self.session_id)
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        res = response.json()
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        # 关闭因为sessionId不正确而没有关闭的会话
        for i in self.sessions:
            ImBaseApi.visitor_close_session(session_id=i)
