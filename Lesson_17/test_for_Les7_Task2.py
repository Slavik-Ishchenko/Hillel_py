﻿import unittest
from Lesson_7 import HW7_Task2


class TempConvertTest(unittest.TestCase):
    """Тест для Lesson_7 -> HW7_Task2"""
    def test_celsius(self):
        """Должен вывести соответствующую конвератцию температур Цельсия"""
        self.assertEqual(HW7_Task2.get_celsius(25), (('Температура в градусах Цельсия: ', 25),
                                                     ('Температура в градусах Фаренгейта: ', 77.0),
                                                     ('Температура в Кельвинах: ', 298.15)))

    def test_fahrenheit(self):
        """Должен вывести соответствующую конвератцию температур Фаренгейта"""
        self.assertEqual(HW7_Task2.get_fahrenheit(35), (('Температура в градусах Цельсия: ', 1.0),
                                                        ('Температура в градусах Фаренгейта: ', 35),
                                                        ('Температура в Кельвинах: ', 274.15)))

    def test_kelvin(self):
        """Должен вывести соответствующую конвератцию температур Кельвина"""
        self.assertEqual(HW7_Task2.get_kelvin(60), (('Температура в градусах Цельсия: ', -213.14999999999998),
                                                    ('Температура в градусах Фаренгейта: ', -352.0),
                                                    ('Температура в Кельвинах: ', 60)))


if __name__ == '__main':
    unittest.main()