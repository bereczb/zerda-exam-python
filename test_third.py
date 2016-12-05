import unittest
import third

class python_exam(unittest.TestCase):

    def test_string_and_letter(self):
        self.assertEqual(third.count_letter_in_string('abcabcabc', 'b'), 3)

    def test_first_param_not_string_but_number(self):
        self.assertEqual(third.count_letter_in_string(5, '5'), 0)

    def test_first_param_not_string_but_list(self):
        self.assertEqual(third.count_letter_in_string([1, 2, 3, 4, 5], 1), 0)

    def test_empty_string(self):
        self.assertEqual(third.count_letter_in_string('', '0'), 0)

    def test_one_missing_parameter(self):
        self.assertRaises(TypeError, third.count_letter_in_string, 'a')

    def test_two_missing_parameter(self):
        self.assertRaises(TypeError, third.count_letter_in_string)

if __name__ == '__main__':
    unittest.main()
