# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name:handle_request.py 
@author: gaojie
@time:  2021/8/3 11:07 
@function：
-------------------------------------------------
"""
import time
import random
import datetime
from requests import request
from common.handle_data import EnvData
from unittest import TestCase
from common.handle_config import conf
from common.handle_openapi import HandleOpenapi
from common.handle_log import log
from common.config import *


class HandleRequest:
    @staticmethod
    def request_response(case):
        """
        判断接口请求，并返回响应的返回值
        :return: response结果
        """
        headers = eval(config.get("env", "headers"))
        data = HandleRequest.replace_data(case=case)
        print(data)
        # 请求方法
        method = case["method"]
        path = case["interface"]

        if method == "GET":
            api = HandleOpenapi(path=path, method=method)
            url = api.sign(s=data)
            response = request(method=method, url=url, headers=headers, timeout=8)
            print(url)
            return response
        elif method == "POST":
            data = eval(data)
            api = HandleOpenapi(path=path, method=method)
            url = api.sign()
            print(url)
            if case["content-type"] == "json":
                response = request(method=method, url=url, json=data, headers=headers, timeout=20)
                return response
            else:
                response = request(method=method, url=url, files=data, headers=headers, timeout=20)
                return response
        else:
            return "Method is not 'GET' or 'POST'"

    @staticmethod
    def assert_res(self, expected, status_code, case, response, excel, row):
        """
        断言方法的封装
        """
        try:
            TestCase.assertEqual(self, expected["status_code"], status_code)
        except AssertionError as e:
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(response.json()))
            log.exception(e)
            # 结果回写excel中
            excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            excel.write_data(row=row, column=8, value="通过")

    @staticmethod
    def get_current_stamp():
        """获取当天的开始时间，结束时间戳"""

        # 今天日期
        today = datetime.date.today()
        # 昨天时间
        yesterday = today - datetime.timedelta(days=1)
        # 明天时间
        tomorrow = today + datetime.timedelta(days=1)
        acquire = today + datetime.timedelta(days=2)
        # 昨天开始时间戳
        yesterday_start_time = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        # 昨天结束时间戳
        yesterday_end_time = int(time.mktime(time.strptime(str(today), '%Y-%m-%d'))) - 1
        # 今天开始时间戳
        today_start_time = str(yesterday_end_time + 1)
        # 今天结束时间戳
        today_end_time = str(int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d'))) - 1)
        # # 明天开始时间戳
        # tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')))
        # # 明天结束时间戳
        # tomorrow_end_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
        # 获取格式化日期2021-09-03
        date = time.strftime("%Y-%m-%d", time.localtime())
        # 获取形如2021-09-03 18:59:59的时间
        date_start_time = date + " 00:00:00"
        date_end_time = date + " 23:59:59"
        # YYMMDD格式的日期20210903
        date1 = date.split("-")
        today_date = ''.join(date1)
        return today_start_time, today_end_time, date, today_date, date_start_time, date_end_time

    @staticmethod
    def random_phone():
        """生成一个手机号"""
        while True:
            phone = "139"
            number = random.randint(10000000, 99999999)
            phone += str(number)
            return phone

    @staticmethod
    def replace_data(case):
        """替换接口用例数据"""
        data = case["data"]
        # 替换data中的数据准备
        date_time = HandleRequest.get_current_stamp()
        name = "新增客户资料" + str(time.time())
        # 在线客服聊天座席
        cno = config.get("im_sdk", "cno")
        # 呼叫sdk座席
        call_cno = config.get("call_sdk", "cno")
        # 座席设置座席
        setting_cno = config.get("clink2_setting", "setting_cno")
        # 呼叫号码
        call_tel = config.get("call_sdk", "tel")
        # 客户资料ID
        # customer_id = str(getattr(EnvData, "customer_id"))
        # session_id = getattr(EnvData, "session_id")
        # session_start_time = getattr(EnvData, "session_start_time")
        if case["data"]:
            # 开始时间时间戳
            data = data.replace("#startTime#", date_time[0])
            # 结束时间时间戳
            data = data.replace("#endTime#", date_time[1])
            # 修改时间戳
            data = data.replace("#updateStartTime#", date_time[0])
            data = data.replace("#updateEndTime#", date_time[1])
            # YYMMDD格式的日期20210903
            data = data.replace("#date#", date_time[3])
            # 获取形如2021-09-03 18:59:59的时间
            data = data.replace("#dateStartTime#", date_time[4])
            data = data.replace("#dateEndTime#", date_time[5])
            data = data.replace("#name#", name)
            data = data.replace("#tel#", HandleRequest.random_phone())
            data = data.replace("#cno#", cno)
            # data = data.replace("#session_id#", session_id)
            # data = data.replace("#sessionTime#", session_start_time)
            data = data.replace("#call_cno#", call_cno)
            data = data.replace("#call_tel#", call_tel)
            data = data.replace("#setting_cno#", setting_cno)
            # data = data.replace("#id#", customer_id)
        return data


if __name__ == '__main__':

    sss = HandleRequest.get_current_stamp()
    print(sss, type(sss))
    print(sss[0], type(sss[0]))
    print(sss[4], type(sss[4]))
    print(sss[5], type(sss[5]))
