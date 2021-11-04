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


# import sys
# sys.path.append('/')
#
#
# DIR = sys.argv[1]
# print(type(DIR))
# print('haha')
# from common.handle_path import CASE_DIR, REPORT_DIR, DEMO_DIR as call_success
#
# print(call_success)
# call_success = call_success.split('\\',-1)
# print(call_success[-1])

import os
import time
from datetime import datetime
from urllib.parse import quote
from urllib import parse
import hmac
from hashlib import sha1
import base64
from urllib.parse import urlencode


class HandleOpenapi:

    protocol = 'https'
    host = 'api-bj.clink.cn'
    expires = '86400'
    access_key_secret = '258J5rPW079H9wLT74V8'
    access_key_id = '12ead894f3481e001630f1308b134112'
    """生成请求openapi的请求地址"""

    def __init__(self, path, method, protocol=protocol, host=host, expires=expires, access_key_secret=access_key_secret,
                 access_key_id=access_key_id):
        # 获取时间戳并进行url转码
        timestamp = quote(HandleOpenapi.get_utc_time())
        self.path = path
        self.method = method
        self.timestamp = timestamp

    def sign(self, s=None):
        # 排序后url
        if s:
            s = HandleOpenapi.encoded_params(param=s)
            temp_url = self.host + "/" + self.path + "?AccessKeyId=" + self.access_key_id + "&Expires=" + self.expires + \
                       "&Timestamp=" + self.timestamp + "&" + s
        else:
            temp_url = self.host + "/" + self.path + "?AccessKeyId=" + self.access_key_id + "&Expires=" + self.expires + \
                       "&Timestamp=" + self.timestamp
        # print("排序编码后url:",temp_url)
        url_param = self.method + temp_url
        # 对签名进行url编码
        signature = quote(HandleOpenapi.hash_hmac(url_param, self.access_key_secret, sha1))
        # 加上签名后的url
        result = temp_url + '&Signature=' + signature
        res = self.protocol + "://" + result
        # print("加上签名后的url:", res)
        return res

    @staticmethod
    def get_utc_time():
        """
        #     获取当前时间，返回iso 8601格式的时间戳
        #     :return: 返回iso 8601格式的时间戳
        #     """
        time1 = datetime.utcfromtimestamp(int(time.time()))
        utc_time = time1.strftime("%Y-%m-%dT%H:%M:%SZ")
        return utc_time

    @staticmethod
    def hash_hmac(code, key, sha1):
        """
        HMACSHA1加密，返回Base64编码
        :param code:
        :param key:
        :param sha1:
        :return:
        """
        hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
        return base64.b64encode(hmac_code).decode()

    @staticmethod
    def encoded_params(param):
        dic = parse.parse_qs(param)

        for key in dic:
            s = dic[key][0]
            dic[key] = s

        encoded_data = urlencode(dic)
        return encoded_data


if __name__ == '__main__':
    # api = HandleOpenapi(path='copy_chat_records', method='GET')
    api = HandleOpenapi(path='online', method='POST')
    ur = api.sign(s="date=20210927")

    print(ur)