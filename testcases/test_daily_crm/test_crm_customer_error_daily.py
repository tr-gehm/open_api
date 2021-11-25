# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_call_create_client.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
客户资料查询，新增删除,异常场景
"""

from base_utils import *


sheet_name = "test_crm_customer_error"
filename = os.path.join(DAILY_DIR_DATA, "crm_apicases_daily.xlsx")


@ddt
class TestCustomerErrorTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        global customer_id
        customer_id = base_api_crm.CrmBaseApi.create_customer()

    @data(*cases)
    def test_call_client_common(self, case):
        expected = eval(case["expected"])
        if case.get("actual"):
            actual = eval(case.get("actual"))
        else:
            actual = None
        row = case["case_id"] + 1
        self.response = HandleRequest.request_response(case)

        status_code = self.response.status_code

        # 断言
        HandleRequest.assert_res(self, expected, status_code, case, self.response, self.excel, row, actual)

    @classmethod
    def tearDownClass(cls):
        """
        删除新增的条件
        """
        base_api_crm.CrmBaseApi.delete_customer(customer_id=customer_id)


if __name__ == '__main__':
    unittest.main()
