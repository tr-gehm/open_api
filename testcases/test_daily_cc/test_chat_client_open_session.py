# -*- coding: utf-8 -*-
"""
-------------------------------------------------
@File Name: test_im_open_api.py
@author: gaojie
@time:  2021/9/4 10:56
@function：
-------------------------------------------------
"""
from base_utils import *
#
sheet_name = "chat_client_open_session"
filename = os.path.join(DATA_DIR, "im_apicases.xlsx")


@ddt
class TestChatClientOpenSessionTestCase(unittest.TestCase):
    excel = HandleExcel(filename, sheet_name)
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        """
        预置条件：只有座席登录置闲的状态下访客才能成功接入
        """
        OpenSession().open_session()
        time.sleep(15)

    @data(*cases)
    def test_chat_client_open_session(self, case):
        # 第一步：准备用例数据
        expected = eval(case["expected"])
        row = case["case_id"] + 1

        # 第二步：发送请求获取实际结果
        response = HandleRequest.request_response(case)
        res = response.json()
        print(res)
        try:
            self.session_id = jsonpath(res, "$..sessionId")[0]
            print(self.session_id)
        except:
            print('会话失败')
        # 获取实际结果
        self.status_code = response.status_code
        # 第三步：断言
        HandleRequest.assert_res(self, expected, self.status_code, case, response, self.excel, row)

    def tearDown(self):
        # 座席关闭会话
        ImBaseApi.client_close_session(session_id=self.session_id)


if __name__ == '__main__':
    unittest.main()