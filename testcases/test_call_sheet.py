# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_im_open_api.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
呼叫中心报表、监控、数据、增值功能接口
"""

import os
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DATA_DIR

sheet_name = "test_call_sheet"
filename = os.path.join(DATA_DIR, "call_apicases.xlsx")


@ddt
class TestCallSheetTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_call_sheet(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)

        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)
