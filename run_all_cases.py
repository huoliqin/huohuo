import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner

#查找用例的目录

start_dir = "D:\\test\\cases"
all = unittest.defaultTestLoader.discover(start_dir, pattern="t*.py")

print(all)

fp = open("D:\\test\\report\\result.html", "wb")

runner = HTMLTestRunner(stream=fp, title="报告的标题",description="报告")

runner.run(all)