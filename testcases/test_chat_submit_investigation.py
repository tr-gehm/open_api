# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_chat_submit_investigation.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
appId对应的导航：北京平台“高杰SDK测试”
"""

import os
import time
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DATA_DIR
from base.base_api_im import ImBaseApi

sheet_name = "chat_submit_investigation"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class ChatSubmitInvestigationTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        ImBaseApi.cno_login()

    def setUp(self):
        """
        发起会话,发起满意度评价
        :return:
        """
        self.session_id = ImBaseApi.visitor_open_session()
        time.sleep(3)
        ImBaseApi.client_investigation(session_id=self.session_id)
        time.sleep(3)

    @data(*cases)
    def test_chat_submit_investigation(self, case):
        # 第一步：准备用例数据
        case["data"] = case["data"].replace("#sessionId#", self.session_id)
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求获取实际结果
        # response = request(method=method, url=url, json=data, headers=headers)
        response = HandleRequest.request_response(case)
        res = response.json()
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        # 关闭因为sessionId不正确而没有关闭的会话
        ImBaseApi.visitor_close_session(session_id=self.session_id)
