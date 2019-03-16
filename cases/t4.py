import unittest
import time

def add(a, b):
    c = a + b
    return c

class TestAdd(unittest.TestCase):
    def setUp(self):
        '''前置操作，所有用例之前都会执行一次'''
        print("打开浏览器")

    def test_add(self):
        time.sleep(1)
        print("执行第一个用例")
        '''测试数据'''
        r = add(2, 4)
        exp = 6
        self.assertEqual(r, exp)
    def test_add2(self):
        time.sleep(1)
        print("执行第二个用例")
        r = add("hello", "world")
        exp = "helloworld"
        self.assertEqual(r, exp)
    def tearDown(self):
        '''数据清理，后置操作！所有用例之后都会执行'''
        time.sleep(1)
        print("关闭浏览器")

if __name__ == "__main__":
    unittest.main()