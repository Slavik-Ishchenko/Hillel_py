import unittest
from Lesson_6 import HW6_Task1


class CoinCodeTest(unittest.TestCase):
    """Тест для Lesson_6 -> HW6_Task1"""
    def test_make_dict(self):
        """Должен создать словарь, типа {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'}
        путем соединения"""
        coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
        code = ('BTC', 'ETH', 'XRP', 'LTC')
        self.assertEqual(HW6_Task1.make_dict(coin, code), {'Bitcoin': 'BTC', 'Ether': 'ETH',
                                                           'Ripple': 'XRP', 'Litecoin': 'LTC'})


if __name__ == '__main':
    unittest.main()

