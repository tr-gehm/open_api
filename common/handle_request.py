# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name:handle_request.py 
@author: gaojie
@time:  2021/8/3 11:07 
@function：
-------------------------------------------------
"""
import json
import time
import random
import datetime


import urllib3
from requests import request
from unittest import TestCase
from common.handle_config import conf
from common.handle_openapi import HandleOpenapi
from common.handle_log import log
from common.handle_context import Context
from common.config import *


class HandleRequest:
    @staticmethod
    def request_response(case):
        """
        判断接口请求，并返回响应的返回值
        :return: response结果
        """
        headers = eval(config.get("env", "headers"))
        sms_headers = eval(config.get("env", "sms_headers"))

        # data = HandleRequest.replace_data(case=case)

        data = Context().re_replace(case['data'])
        # 请求方法
        method = case["method"]
        path = case["interface"]

        if method == "GET":
            api = HandleOpenapi(path=path, method=method)
            if data == 'None':
                url = api.sign()
            else:
                url = api.sign(s=data)
            log.info("请求url：{}".format(url))
            log.info("请求数据：{}".format(data))
            response = request(method=method, url=url, headers=headers, timeout=8)
            return response
        elif method == "POST":
            data = eval(data)
            api = HandleOpenapi(path=path, method=method)
            url = api.sign()
            log.info("请求url：{}".format(url))
            log.info("请求数据：{}".format(data))
            if case["content-type"] == "json":
                response = request(method=method, url=url, json=data, headers=headers, timeout=20)
                return response
            elif case["content-type"] == "form-data":
                response = request(method=method, url=url, files=data, timeout=20)
                return response
            else:
                # response = request(method=method, url=url, files=data, headers=headers, timeout=20)
                response = request(method=method, url=url, json=data, headers=sms_headers, timeout=20)
                return response
        else:
            return "Method is not 'GET' or 'POST'"

    @staticmethod
    def clink2_request(case):
        """clink2 页面接口专用"""
        # 测试数据进行转换,替换参数
        if case["data"] != None:
            data = json.loads(Context().re_replace(case["data"]))
        # 获取请求方法
        url = Context().re_replace(case["interface"])
        method = case["method"]
        # 根据客户端不同 获取不同的header。url
        if case["target"] == 'console':
            cookies = Context().re_replace({"Cookie":"#console_cookie#"})
            cookies = json.loads(cookies.replace("'",'"'))
            url = config.get('env', 'base_console_url') + url
        else:
            cookies = Context().re_replace({"Cookie":"#agent_cookie#"})
            cookies = json.loads(cookies.replace("'", '"'))
            url = config.get('env', 'base_agent_url') + url
        if method.lower() == 'get':
            log.info("请求url：{}".format(url))
            resp = request(method=method, url=url, cookies=cookies, verify=False)
        elif method.lower() == 'post':
            log.info("请求url：{}".format(url))
            log.info("请求数据：{}".format(data))
            if case["content-type"] == "json":
                resp = request(method=method, url=url, json=data, cookies=cookies,  verify=False)
            else:
                resp = request(method=method, data=data, cookies=cookies,  verify=False)
        elif method.lower() == 'put':
            log.info("请求url：{}".format(url))
            log.info("请求数据：{}".format(data))
            if case["content-type"] == "json":
                resp = request(method=method,url=url, json=data, cookies=cookies, verify=False)
            else:
                resp = request(method=method, url=url, data=data, cookies=cookies, verify=False)
        elif method.lower() == 'delete':
            log.info("请求url：{}".format(url))
            resp = request(method=method, url=url, cookies=cookies, verify=False)

        return resp

    @staticmethod
    def assert_res(self, expected, status_code, case, response, excel, row):
        """
        断言方法的封装
        """

        try:
            TestCase.assertEqual(self, expected["status_code"], status_code)
        except AssertionError as e:
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.info("预期结果：{}".format(expected))
            log.info("实际结果：{}".format(response.json()))
            log.exception(e)
            # 结果回写excel中
            excel.write_data(row=row, column=8, value=response.text)
            excel.write_data(row=row, column=9, value="未通过")
            raise e
        else:
            # 结果回写excel中
            excel.write_data(row=row, column=9, value="通过")

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



if __name__ == '__main__':
    sss = HandleRequest.get_current_stamp()
    print(sss, type(sss))
    print(sss[0], type(sss[0]))
    print(sss[4], type(sss[4]))
    print(sss[5], type(sss[5]))

    date_time = HandleRequest.get_current_stamp()
    print(date_time[0])
