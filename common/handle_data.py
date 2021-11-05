# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: handle_data.py
@author: gaojie
@time:  2021/9/12 19:56
@function：
-------------------------------------------------
"""

import time

import jsonpath

from common.handle_request import HandleRequest


class EnvData:
    """
    用于参数传递，获取动态参数
    """
    a = HandleRequest
    date_time = a.get_current_stamp()
    startTime = date_time[0]
    endTime = date_time[1]
    updateStartTime = date_time[0]
    updateEndTime = date_time[1]
    date = date_time[3]
    dateStartTime = date_time[4]
    dateEndTime = date_time[5]
    name = "新增客户资料" + str(time.time())
    tel = a.random_phone()


    def re_par(self, par, resp):
        """
        par: 列表格式
        resp：请求返回值
        """
        for exp in par:
            for k,v in exp.items():
                cashu = jsonpath.jsonpath(resp,v)
                setattr(EnvData, k, cashu[0])
            return '传参成功'
        else:
            return '不需要替换参数'


if __name__ == '__main__':
    setattr(EnvData, 'ivrID', 'ivrID')
    print(getattr(EnvData, 'date'))
    # print(hasattr(EnvData, 'ivrID'))

