# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: handle_path.py
@author: gaojie
@time:  2021/8/2 19:56
@function：
-------------------------------------------------
"""

import os

# 获取项目所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例模块所在的目录路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")

# 用例模块所在的目录路径
DEMO_DIR = os.path.join(BASE_DIR, "testcases", "test_call_demo")

# 用例数据所在的目录路径
DATA_DIR = os.path.join(BASE_DIR, "data")

# 配置文件所在的目录路径
CONF_DIR = os.path.join(BASE_DIR, "conf")
# TEST2环境配置
TEST2_CONF = os.path.join(BASE_DIR, "conf", 'config_test2.ini')
# 线上环境配置
ONLINE_CONF = os.path.join(BASE_DIR, "conf", 'config.ini')
# 环境开关路径
GLOBAL_FILE = os.path.join(BASE_DIR, "conf", 'global.conf')

# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 日志文件所在的目录路径
LOG_DIR = os.path.join(BASE_DIR, "logs")

if __name__ == '__main__':
    print(DEMO_DIR)

