import unittest
from Lesson_11 import HW11_Task2


class EmailCheckTest(unittest.TestCase):
    """Должен шифровать Email_address по аналогии slavik228@gmail.com -> sla******@***il.com (по символу "@")"""
    def test_email_check(self):
        email = HW11_Task2.hide_email('slavik228@gmail.com')
        self.assertEqual(email, 'sla******@***il.com')


if __name__ == '__main':
    unittest.main()
