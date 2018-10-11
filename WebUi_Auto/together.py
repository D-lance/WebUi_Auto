# coding=utf-8

# 此用例用于多条case调试

import unittest
from test_case.test_case_1.start_case_01 import Case_01
# from test_case.test_case_1.start_case_09 import Case_09
# from test_case.test_case_2.start_case_06 import Case_06


#构造测试集
suite = unittest.TestSuite()
suite.addTest(Case_01("test_login"))
# suite.addTest(Case_09("test_order"))
# suite.addTest(Case_06("test_Contactlenses"))

#suite.addTest(shiyongzhongxin("test_syzx"))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
