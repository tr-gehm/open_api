# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 14:11
@Auth ： ghm
@File ：chose_case.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from common.handle_path import *


class ChoseCase:

    def chosedir(self, case):
        """
        根据关键词执行对应的测试用例。
        """
        print(case)
        if case == 'daily':
            DIR = DAILY_CALL_DIR
        elif case == 'daily_c2':
            DIR = DAILY_C2_CALL_DIR
        elif case == 'daily_crm':
            DIR = DAILY_CRM_DIR
        elif case == 'all':
            DIR = CASE_DIR
        else:
            return 'BYEBYE'
        return DIR


if __name__ == '__main__':
    print(ChoseCase().chosedir('adf'))