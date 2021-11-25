"""
-------------------------------------------------
@File Name: test_mainstream_visitor.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
访客发起会话到结束会话流程
"""

import os
import unittest
from unittestreport import rerun
from common.handle_config import conf
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from base.base_api_im import ImBaseApi
from common.handle_request import HandleRequest
from library.myddt import ddt, data

filename = os.path.join(DATA_DIR, "im_apicases.xlsx")
# headers = eval(conf.get("env", "headers"))
sheet_name = "main_stream_visitor"


@ddt
class TestMainStream(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        座席登录
        :return:
        """
        # 座席登录
        ImBaseApi.cno_login()
        # 访客发起会话
        cls.sessionId = ImBaseApi.visitor_open_robot_session()

    @data(*cases)
    @rerun(count=3, interval=2)
    def test_main_stream_visitor(self, case):
        # 准备数据
        case["data"] = case["data"].replace("#sessionId#", self.sessionId)
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        if case["interface"] == "chat_submit_investigation":
            ImBaseApi.client_investigation(session_id=self.sessionId)
        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    @classmethod
    def tearDownClass(cls):
        ImBaseApi.visitor_close_session(cls.sessionId)
