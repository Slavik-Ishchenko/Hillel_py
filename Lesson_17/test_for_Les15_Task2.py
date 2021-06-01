import unittest
from Lesson_15 import HW15_Task2


class PhoneNumberTest(unittest.TestCase):
    """Должен форматрировать номер телефона по аналогиии -> (+38) 063 999-99-99"""
    def test_phone_number(self):
        self.assertEqual(HW15_Task2.format_number('0639999999'), '(+38) 063 999-99-99')
        self.assertEqual(HW15_Task2.format_number('063-999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(HW15_Task2.format_number('063 999-99-99'), '(+38) 063 999-99-99')
        self.assertEqual(HW15_Task2.format_number('063-99999-99'), '(+38) 063 999-99-99')
        self.assertEqual(HW15_Task2.format_number('+3806399-999-99'), '(+38) 063 999-99-99')
        self.assertEqual(HW15_Task2.format_number('+380639999999'), '(+38) 063 999-99-99')


if __name__ == '__main':
    unittest.main()
