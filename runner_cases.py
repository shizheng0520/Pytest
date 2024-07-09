import unittest
from BeautifulReport import BeautifulReport

#执行批量的测试用例
suite = unittest.defaultTestLoader.discover(start_dir = r'C:\python_auto\unitest\test_demo', pattern = 'test*.py')

#Text 的测试报告
# runner = unittest.TextTestRunner()
# runner.run(suite)

result = BeautifulReport(suite)
result.report(description='系统登陆的测试报告', filename='SIT测试报告', report_dir=r'C:\python_auto\unitest\report')