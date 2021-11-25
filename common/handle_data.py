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
import jmespath

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
    today_time = date_time[-1]
    name = "新增客户资料" + str(time.time())
    tels = a.random_phone()

    def re_par(self, par, resp):
        """
        par: 列表格式
        resp：请求返回值
        """
        error_list = []
        if isinstance(par, list):
            for exp in par:
                for k,v in exp.items():
                    cashu = jmespath.search(v, resp)
                    if cashu:
                        setattr(EnvData, k, cashu)
                    elif cashu == 0:
                        setattr(EnvData, k, cashu)
                    else:
                        setattr(EnvData, k, None)
                        error_list.append(k)
            return (f'转换成功,该字段--{error_list}--没有正常转换，手动转为None')
        else:
            return (f'{par}格式错误')


if __name__ == '__main__':
   setattr(EnvData, 'DEMO', None)
   print(type(getattr(EnvData, 'DEMO')))



