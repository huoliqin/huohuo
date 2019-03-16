import unittest

def add(a, b):
    c = a + b
    return c

class TestAdd(unittest.TestCase):
    def test_add(self):
        '''测试数据'''
        r = add(2, 4)
        exp = 6
        self.assertEqual(r, exp)
    def test_add2(self):
        r = add("hello", "world")
        exp = "helloworld"
        self.assertEqual(r, exp)
if __name__ == "__main__":
    unittest.main()