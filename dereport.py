import unittest
from config import path1,reportfile1
from ClassicHTMLTestRunner import HTMLTestRunner
from lib.sendmail import send_email
suite=unittest.defaultTestLoader.discover('demo',pattern='demo_unittest*.py')
reportFile=open(path1,'wb')
runner=HTMLTestRunner(stream=reportFile,verbosity=2,description='用例执行明细',
                       title='xxx项目的测试报告',tester='曹伟')
runner.run(suite)
send_email()