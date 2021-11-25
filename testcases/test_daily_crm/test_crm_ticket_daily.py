# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_call_create_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
工单新增查询 等正向用例
"""

from base_utils import *


sheet_name = "test_ticket"
filename = os.path.join(DAILY_DIR_DATA, "crm_apicases_daily.xlsx")


@ddt
class TestTicketTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_call_client_common(self, case):
        expected = eval(case["expected"])
        if case.get("actual"):
            actual = eval(case.get("actual"))
        else:
            actual =None
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)

        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row, actual)


if __name__ == '__main__':
    unittest.main()
