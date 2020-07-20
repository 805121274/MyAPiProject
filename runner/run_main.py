import time
import unittest

from path_dir import case_path,report_dir
from runner.HTMLTestRunner import HTMLTestRunner

def run_case(dir = "testcase"):
    discover= unittest.defaultTestLoader.discover(case_path,pattern="test_*.py",top_level_dir=None)
    return discover

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    reporturl = report_dir +current_time+"-Report.html"
    with open(reporturl, 'wb+') as f:  # 在python3，要写成'wb' or 'wr'
        runner = HTMLTestRunner(stream=f, title='Report', description='api auto report',
                                verbosity=2)
        runner.run(run_case())