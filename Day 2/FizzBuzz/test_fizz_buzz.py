import unittest
import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """
        Test Cases for the fizz_buzz function
    """

    # Testing if function returns 'Fizz' for input 3
    def test_fizz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(3), 'Fizz', msg='should return `Fizz` for number divisible by 3')

    # Testing if function returns 'Fizz' for input 33
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(33), 'Fizz', msg='should return `Fizz` for number divisible by 3')

    # Testing if function returns 'Buzz' for input 5
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(5), 'Buzz', msg='should return `Buzz` for number divisible by 5')

    # Testing if function returns 'Buzz' for input 25
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(25), 'Buzz', msg='should return `Buzz` for number divisible by 5')

    # Testing if function returns 'FizzBuzz' for input 15
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(15), 'FizzBuzz',
                         msg='should return `FizzBuzz` for number divisible by 3 and 5')

    # Testing if function returns 'FizzBuzz' for input 105
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(105), 'FizzBuzz',
                         msg='should return `FizzBuzz` for number divisible by 3 and 5')

    # Testing if function returns 101 for input 101 that is neither divisible by 3 or 5
    def test_indivisible_1(self):
        self.assertEqual(fizz_buzz.fizz_buzz(101), 101,
                         msg='should return the number if its in divisible by neither 3 or 5')

    # Testing if function returns 8 for input 8 that is neither divisible by 3 or 5
    def test_indivisible_2(self):
        self.assertEqual(fizz_buzz.fizz_buzz(8), 8,
                         msg='should return the number if its in divisible by neither 3 or 5')


if __name__ == "__main__":
    unittest.main()
