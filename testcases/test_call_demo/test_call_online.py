# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_im_open_api.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
呼叫座席上线
"""

import os
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from base.base_api_call import CallBaseApi
from library.myddt import ddt, data
from common.handle_path import DATA_DIR

sheet_name = "test_call_online"
filename = os.path.join(DATA_DIR, "call_apicases.xlsx")


@ddt
class TestCallOnlineTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_call_online(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)

        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)

    def tearDown(self):
        CallBaseApi.offline()
