# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name:test_chat_client_investigation.py 
@author: gaojie
@time:  2021/9/16 2:22 下午 
@function：
-------------------------------------------------
"""
# import os
# import time
# import unittest
# from common.handle_data import EnvData
# from jsonpath import jsonpath
# from common.handle_excel import HandleExcel
# from common.handle_request import HandleRequest
# from library.myddt import ddt, data
# from common.handle_path import DATA_DIR
# from base.base_api_im import ImBaseApi
#
# sheet_name = "chat_client_investigation"
# filename = os.path.join(DATA_DIR, "im_apicases.xlsx")
#
#
# @ddt
# class ChatClientInvestigationTestCase(unittest.TestCase):
#     excel = HandleExcel(filename, sheet_name)
#     cases = excel.read_data()
#
#     @classmethod
#     def setUpClass(cls):
#         """
#         预置条件：只有座席登录置闲的状态下访客才能成功接入
#         """
#         ImBaseApi.cno_login()
#         time.sleep(3)
#         cls.session_id = ImBaseApi.visitor_open_session()
#         time.sleep(3)
#         ImBaseApi.client_chat_message_to_visitor(session_id=cls.session_id)
#         ImBaseApi.visitor_close_session(session_id=cls.session_id)
#         time.sleep(20)
#         setattr(EnvData, "session_id", cls.session_id)
#         cls.session_start_time = cls.session_id.split(".")[1] + "000"
#         setattr(EnvData, "session_start_time", cls.session_start_time)
#
#     def setUp(self):
#         ImBaseApi.client_open_session()
#         time.sleep(3)
#
#     @data(*cases)
#     def test_chat_client_investigation(self, case):
#         # 第一步：准备用例数据
#         expected = eval(case["expected"])
#         row = case["case_id"] + 1
#
#         # 第二步：发送请求获取实际结果
#         response = HandleRequest.request_response(case)
#
#         # 获取实际结果
#         self.status_code = response.status_code
#
#         # 第三步：断言
#         HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)
#
#     def tearDown(self):
#         # 座席关闭会话
#         ImBaseApi.client_close_session(session_id=self.session_id)
