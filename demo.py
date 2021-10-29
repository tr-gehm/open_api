# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/27 9:50
@Auth ： ghm
@File ：demo.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

# """
# from common.handle_excel import HandleExcel
# import os
# from common.handle_path import DATA_DIR
# from common.handle_request import HandleRequest
#
# sheet_name = "test_call_create_client"
# filename = os.path.join(DATA_DIR, "call_apicases.xlsx")
# excel = HandleExcel(filename, sheet_name)
# cases = excel.read_data()[0]
# print(cases)
# data = HandleRequest.replace_data(case=cases)
# print(data)


import sys
sys.path.append('/')


DIR = sys.argv[1]
print(type(DIR))
print('haha')
# from common.handle_path import CASE_DIR, REPORT_DIR, DEMO_DIR as call_success
#
# print(call_success)
# call_success = call_success.split('\\',-1)
# print(call_success[-1])