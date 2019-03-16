import unittest
from selenium import webdriver
class TestAdd(unittest.TestCase):

    def setUp(self):
        #self代表TestAdd这个类
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_id("kw").send_keys("youyou")

    def test_02(self):
        self.driver.find_element_by_id("kw").send_keys("ok")
        self.assertEqual(1,2)

if __name__ == "__main__":
    unittest.main()