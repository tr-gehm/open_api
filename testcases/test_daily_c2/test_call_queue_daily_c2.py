# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_call_create_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
队列回归用例：新增、修改、删除、查询、查看详情
"""

import os
import unittest
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DAILY_C2_DIR_DATA
from base.base_clink2_console import Clink2Console
from common.handle_data import EnvData

sheet_name = "test_call_queue"
filename = os.path.join(DAILY_C2_DIR_DATA, "call_apicases_daily.xlsx")


@ddt
class TestCallQueueTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        Clink2Console.login()

    @data(*cases)
    def test_call_queue_common(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.clink2_request(case)
        if case['case_id'] == 2:
            queue_id = self.response.json().get('result').get('data')[0].get('id')
            setattr(EnvData, 'queue_id', queue_id)
        status_code = self.response.status_code
        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)


if __name__ == '__main__':
    unittest.main()
