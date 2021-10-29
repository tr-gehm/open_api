import unittest
from common.handle_path import CASE_DIR, REPORT_DIR, DEMO_DIR
from unittestreport import TestRunner
from common.send_email import send_email
from common.config import *
import sys
sys.path.append('/')
# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(DEMO_DIR))

runner = TestRunner(suite,
                    filename="api_call_success.html",
                    report_dir=REPORT_DIR,
                    title='clink2_call_success测试报告',
                    tester='demo',
                    desc="clink2_call_success接口测试报告",
                    templates=2)
runner.run()

runner.send_email(
    host=config.get('email', 'host'),
    port=465,
    user=config.get('email', 'user'),
    password=config.get('email', 'password'),
    to_addrs="1010562639@qq.com")

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
