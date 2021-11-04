"""
-------------------------------------------------
@File Name: test_update_customer.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
"""
import os
import unittest
from jsonpath import jsonpath
from unittestreport import rerun
from common.handle_config import conf
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from base.base_api_crm import CrmBaseApi
from common.handle_request import HandleRequest
from library.myddt import ddt, data
from base.base_api_crm import CrmBaseApi
from common.handle_data import EnvData
from requests import request

filename = os.path.join(DATA_DIR, "business_apicases.xlsx")
sheet_name = "test_update_customer"


@ddt
class TestCustomer(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    def setUp(self):
        self.customer_id = CrmBaseApi.create_customer()
        setattr(EnvData, "customer_id", self.customer_id)

    @data(*cases)
    def test_customer(self, case):
        # 准备数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        case["data"] = case["data"].replace("#id#", str(self.customer_id))
        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        CrmBaseApi.delete_customer(customer_id=self.customer_id)
