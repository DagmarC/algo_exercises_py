import unittest
from dp.how_sum import how_sum_rec


class TestHowSumRec(unittest.TestCase):
    def test_how_sum_rec_1(self):
        target = 7
        arr = [2, 3]
        expected_result = [3, 2, 2]
        got = how_sum_rec(target, arr)
        self.assertEqual(got, expected_result)

    def test_how_sum_rec_2(self):
        target = 7
        arr = [5, 3, 4, 7]
        expected_result = [4, 3]
        got = how_sum_rec(target, arr)
        self.assertEqual(got, expected_result)

    def test_how_sum_rec_3(self):
        target = 7
        arr = [2, 4]
        expected_result = None
        got = how_sum_rec(target, arr)
        self.assertEqual(got, expected_result)

    def test_how_sum_rec_4(self):
        target = 8
        arr = [2, 3, 5]
        expected_result = [2, 2, 2, 2]
        got = how_sum_rec(target, arr)
        self.assertEqual(got, expected_result)

    def test_how_sum_rec_5(self):
        target = 300
        arr = [7, 14]
        expected_result = None
        got = how_sum_rec(target, arr)
        self.assertEqual(got, expected_result)


if __name__ == '__main__':
    unittest.main()
