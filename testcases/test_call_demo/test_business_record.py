"""
-------------------------------------------------
@File Name: test_mainstream_visitor.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
业务记录管理接口
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
sheet_name = "test_business_record"
# headers = eval(conf.get("env", "headers"))


@ddt
class TestBusinessRecord(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @data(*cases)
    def test_business_record(self, case):
        # 准备数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1
        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)

        print(response.json())
        # 获取实际结果
        self.status_code = response.status_code

        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)
