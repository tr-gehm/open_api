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
        if case == 'call_success':
            DIR = DEMO_DIR
        elif input == 'all':
            DIR = CASE_DIR
        else:
            return 'BYEBYE'
        return DIR

if __name__ == '__main__':
    print(ChoseCase().chosedir('adf'))