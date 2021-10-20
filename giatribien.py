import unittest
def get_price(weight):
    if weight > 0.0 and weight < 5.0:
        return 5
    elif weight >= 5.0 and weight < 10.0:
        return 10
    elif weight >= 10.0 and weight < 30.0:
        return 15
    else:
        return "Không hợp lệ"

class TestMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_price(0), 5)

    def test2(self):
        self.assertEqual(get_price(30), 15)

    def test3(self):
        self.assertEqual(get_price(15), 15)

    def test4(self):
        self.assertEqual(get_price(0.1), 5)

    def test5(self):
        self.assertEqual(get_price(29.9), 15)

    def test6(self):
        self.assertEqual(get_price(-0.1), "Không hợp lệ")

    def test7(self):
        self.assertEqual(get_price(30.1), "Không hợp lệ")

if __name__ == '__main__':
    unittest.main()
