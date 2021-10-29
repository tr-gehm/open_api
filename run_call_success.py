import unittest
from common.handle_path import REPORT_DIR
from unittestreport import TestRunner
from common.send_email import send_email
from common.chose_case import ChoseCase
from common.config import *
import sys
sys.path.append('/')


input = sys.argv[1]
print(input)
DIR = ChoseCase().chosedir(input)
print(DIR)

# 创建测试套件
suite = unittest.TestSuite()
# 加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(DIR))
runner = TestRunner(suite,
                    filename=f"clink2_{input}.html",
                    report_dir=REPORT_DIR,
                    title=f'clink2_{input}测试报告',
                    tester='demo',
                    desc=f"clink2_{input}接口测试报告",
                    templates=2)
runner.run()

# runner.send_email(
#     host=config.get('email', 'host'),
#     port=465,
#     user=config.get('email', 'user'),
#     password=config.get('email', 'password'),
#     to_addrs="1010562639@qq.com")

# 发送钉钉通知
runner.dingtalk_notice(url=config.get('dingding','url'),
                       key=config.get('dingding','key'),
                       secret=config.get('dingding','secret'))
# 发送邮件
# send_email()
# 多线程
# runner.run(thread_count=5)
# 执行测试用例，失败重运行设置为3次，间隔时间为2秒
# runner.rerun_run(count=3, interval=2)
# send_email()
