# Name:         Sameera Balijepalli

import unittest

import postfixit


class TestOperand(unittest.TestCase):
    def test_operand_1(self):
        item = "0"
        self.assertEqual(postfixit.operand(item), True)

    def test_operand_2(self):
        item = "1"
        self.assertEqual(postfixit.operand(item), True)

    def test_operand_3(self):
        item = "-5"
        self.assertEqual(postfixit.operand(item), True)

    def test_operand_4(self):
        item = "A"
        self.assertEqual(postfixit.operand(item), False)

    def test_operand_5(self):
        item = "C"
        self.assertEqual(postfixit.operand(item), False)

    def test_operand_6(self):
        item = "3.14"
        self.assertEqual(postfixit.operand(item), True)


class TestCalculate(unittest.TestCase):
    def test_calculate_1(self):
        self.assertEqual(postfixit.calculate(3.0, 1.0, "*"), 3.000)

    def test_calculate_2(self):
        self.assertEqual(postfixit.calculate(3.0, 1.0, "+"), 4.000)

    def test_calculate_3(self):
        self.assertEqual(postfixit.calculate(1.0, 3.0, "/"), 3.000)

    def test_calculate_4(self):
        self.assertEqual(postfixit.calculate(3.0, 1.0, "-"), -2.000)

    def test_calculate_5(self):
        self.assertEqual(postfixit.calculate(0.0, 1.0, "*"), 0.000)


class TestPemdas(unittest.TestCase):
    def test_pemdas_1(self):
        item = "*"
        self.assertEqual(postfixit.pemdas(item), 1)

    def test_pemdas_2(self):
        item = "+"
        self.assertEqual(postfixit.pemdas(item), 0)

    def test_pemdas_3(self):
        item = "/"
        self.assertEqual(postfixit.pemdas(item), 1)

    def test_pemdas_4(self):
        item = "-"
        self.assertEqual(postfixit.pemdas(item), 0)

    def test_pemdas_5(self):
        item = "A"
        self.assertEqual(postfixit.pemdas(item), -1)


class TestPostfix(unittest.TestCase):
    def test_postfix_1(self):
        infix = "3 + 4"
        self.assertEqual(postfixit.postfix(infix),
                            "3 4 +")

    def test_postfix_2(self):
        infix = "( 1 + 2 ) * 3"
        self.assertEqual(postfixit.postfix(infix),
                            "1 2 + 3 *")

    def test_postfix_3(self):
        infix = "8 / 4 ^ 3"
        self.assertEqual(postfixit.postfix(infix),
                            "8 4 3 ^ /")

    def test_postfix_4(self):
        infix = "( 3 + 4 ) - 5"
        self.assertEqual(postfixit.postfix(infix),
                            "3 4 + 5 -")

    def test_postfix_5(self):
        infix = "( 3 + 4 ) ^ 7"
        self.assertEqual(postfixit.postfix(infix),
                            "3 4 + 7 ^")


class TestEvaluate(unittest.TestCase):
    def test_evaluate_1(self):
        postfix = "3 4 +"
        self.assertEqual(postfixit.evaluate(postfix),
                            "7.000")
    def test_evaluate_2(self):
        postfix = "1 2 + 3 *"
        self.assertEqual(postfixit.evaluate(postfix),
                            "9.000")
    def test_evaluate_3(self):
        postfix = "8 4 3 ^ /"
        self.assertEqual(postfixit.evaluate(postfix),
                            "0.125")
    def test_evaluate_4(self):
        postfix = "3 4 + 5 -"
        self.assertEqual(postfixit.evaluate(postfix),
                            "2.000")
    def test_evaluate_5(self):
        postfix = "3 4 + 7 ^"
        self.assertEqual(postfixit.evaluate(postfix),
                            "823543.000")


if __name__ == "__main__":
    unittest.main()
