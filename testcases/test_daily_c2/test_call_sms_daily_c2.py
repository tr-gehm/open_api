# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_call_create_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
短信日常回归用例：短信发送，号码检测
"""


from base_utils import *

sheet_name = "test_call_sms"
filename = os.path.join(DAILY_C2_DIR_DATA, "call_apicases_daily.xlsx")


@ddt
class TestCallQueueTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        Clink2Console.login()

    @data(*cases)
    def test_call_sms_common(self, case):
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        self.response = HandleRequest.clink2_request(case)
        status_code = self.response.status_code
        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row)


if __name__ == '__main__':
    unittest.main()
