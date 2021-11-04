"""
-------------------------------------------------
@File Name: test_customer.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
"""

import os
import unittest
from jsonpath import jsonpath
from unittestreport import rerun
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from base.base_api_crm import CrmBaseApi

filename = os.path.join(DATA_DIR, "business_apicases.xlsx")
sheet_name = "test_customer"


@ddt
class TestCustomer(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_customer(self, case):
        # 准备数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求获取实际结果
        self.response = HandleRequest.request_response(case)
        # 获取实际结果
        self.status_code = self.response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, self.response, self.excel, row)

    @data(*cases)
    def tearDown(self, case):
        if case["interface"] == "create_customer":
            self.customer_id = jsonpath(self.response.json(), "$..id")[0]
            CrmBaseApi.delete_customer(customer_id=self.customer_id)
