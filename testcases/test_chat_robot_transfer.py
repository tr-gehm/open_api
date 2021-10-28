# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_chat_robot_transfer.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
chat_robot_transfer:访客转人工
对应的导航:郑忠坡SDK测试
"""

import os
import time
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DATA_DIR
from base.base_api_im import ImBaseApi

sheet_name = "chat_robot_transfer"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class ChatRobotTransferTestCase(unittest.TestCase):
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
        访客转人工的前提：访客发起会话
        """
        self.session_id = ImBaseApi.visitor_open_robot_session()
        time.sleep(3)
    @data(*cases)
    def test_chat_robot_transfer(self, case):
        # 第一步：准备用例数据
        case["data"] = case["data"].replace("#sessionId#", self.session_id)
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        res = response.json()
        # 获取实际结果
        self.status_code = response.status_code
        print(self.status_code)

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        """
        清理会话，避免会话堆积
        :return:
        """
        ImBaseApi.visitor_close_session(self.session_id)
