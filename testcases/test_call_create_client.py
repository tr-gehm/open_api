# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_call_create_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
呼叫座席置闲
"""

import os
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from base.base_api_call import CallBaseApi
from library.myddt import ddt, data
from common.handle_path import DATA_DIR

sheet_name = "test_call_create_client"
filename = os.path.join(DATA_DIR, "call_apicases.xlsx")


@ddt
class TestCallCreateClientTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_call_create_client(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)

        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)

    def tearDown(self):
        CallBaseApi.delete_client()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCallCreateClientTestCase))
    runner = unittest.TextTestRunner()
    runner.run(suite)
