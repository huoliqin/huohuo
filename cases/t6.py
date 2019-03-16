import unittest
from selenium import webdriver
class TestAdd(unittest.TestCase):

    #类方法
    @classmethod
    def setUpClass(cls):
        print("用例之前只执行一次")
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        print("用例最后只执行一次")
        cls.driver.quit()

    # def setUp(self):
    #     #self代表TestAdd这个类
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("https://www.baidu.com")
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("youyou")

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("ok")

if __name__ == '__main__':
    unittest.main()