import unittest
from common.handle_path import CASE_DIR, REPORT_DIR, DEMO_DIR
from unittestreport import TestRunner
from common.send_email import send_email
import sys
sys.path.append('/')
# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(DEMO_DIR))

runner = TestRunner(suite, filename="OpenApi.html", report_dir=REPORT_DIR, title='测试报告', tester='高杰',
                    desc="clink2 OpenApi接口测试报告", templates=1)
runner.run()
send_email()
# 多线程
# runner.run(thread_count=5)
# 执行测试用例，失败重运行设置为3次，间隔时间为2秒
# runner.rerun_run(count=3, interval=2)
# send_email()
