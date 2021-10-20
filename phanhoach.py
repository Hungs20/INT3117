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
        self.assertEqual(get_price(3), 5)

    def test2(self):
        self.assertEqual(get_price(7), 10)

    def test3(self):
        self.assertEqual(get_price(12), 15)

    def test4(self):
        self.assertEqual(get_price(-5), "Không hợp lệ")

    def test5(self):
        self.assertEqual(get_price(35), "Không hợp lệ")

if __name__ == '__main__':
    unittest.main()
