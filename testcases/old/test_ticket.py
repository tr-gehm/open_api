"""
-------------------------------------------------
@File Name: test_mainstream_visitor.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
工单openApi接口
"""

import os
import unittest
from unittestreport import rerun
from common.handle_config import conf
from common.handle_path import DATA_DIR
from common.handle_excel import HandleExcel
from common.handle_request import HandleRequest
from library.myddt import ddt, data

filename = os.path.join(DATA_DIR, "business_apicases.xlsx")
# headers = eval(conf.get("env", "headers"))
sheet_name = "test_ticket"


@ddt
class TestTicket(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_ticket(self, case):
        # 第一步：准备数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        print(response.json())
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)
