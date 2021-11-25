# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_chat_visitor_open_session.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
chat_visitor_open_session:访客发起会话
"""

import os
import time
import unittest
from base.base_api_im import ImBaseApi
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DATA_DIR
from jsonpath import jsonpath

sheet_name = "chat_visitor_open_session"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class ChatVisitorOpenSessionTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        ImBaseApi.cno_login()

    @data(*cases)
    def test_chat_visitor_open_session(self, case):
        # 第一步：准备用例数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        res = response.json()

        # 获取实际结果
        self.status_code = response.status_code
        if self.status_code == 200:
            # 获取会话Id
            self.session_id = jsonpath(res, "$..sessionId")[0]

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        """
        发起成功的会话，清理掉，避免会话堆积
        :return:
        """
        if self.status_code == 200:
            ImBaseApi.visitor_close_session(self.session_id)
