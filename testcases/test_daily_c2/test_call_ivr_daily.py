# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/2 13:45
@Auth ： ghm
@File ：test_call_ivr_daily.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
语音导航回归用例：导航列表，节点查询
"""

import os
import unittest

from common.handle_data import EnvData
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from common.handle_path import DAILY_DIR_DATA

sheet_name = "test_call_ivr"
filename = os.path.join(DAILY_DIR_DATA, "call_apicases_daily.xlsx")


@ddt
class TestCallQueueTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_call_queue_common(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)
        print(self.response.json())
        ivrID = self.response.json().get('ivrs')[0].get('id') if case['case_id'] == 1 else print('pass')
        setattr(EnvData, 'ivrID', ivrID)
        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)


if __name__ == '__main__':
    unittest.main()
