'''test_ehex.py'''

import os
import sys
import unittest

sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__)) + '/../')

from ehex.ehex import ehex

VERSION_INFO = '{0}.{1}'.format(
    sys.version_info[0],
    sys.version_info[1])


class TestEHexBasic(unittest.TestCase):
    '''eHex basic unit tests'''
    def test_assign_invalid(self):
        '''Test invalid assignments'''
        if VERSION_INFO >= '2.7':
            for test_value in [-1, 43, 'I', 'O', 'AA']:
                with self.assertRaises(ValueError):
                    ehex(test_value)
        else:
            for test_value in [-1, 43, 'I', 'O', 'AA']:
                self.assertRaises(ValueError, ehex, test_value)

    def test_assign_valid_int(self):
        '''Test valid int assignment'''
        hexits = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
        for digit in range(0, 33):
            hexit = ehex(digit)
            self.assertTrue(str(hexit) == hexits[digit])

    def test_assign_valid_str(self):
        '''Test valid str assignment'''
        hexits = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZ'
        for hexit in hexits:
            ehx = ehex(hexit)
            self.assertTrue(int(ehx) == hexits.find(str(ehx)))


class TestEHexComparison(unittest.TestCase):
    '''eHex comparison unit tests'''
    def test_compare_int(self):
        '''Test int comparisons'''
        hexit = ehex(7)
        self.assertTrue(hexit == 7)
        self.assertTrue(hexit >= 7)
        self.assertTrue(hexit > 6)
        self.assertTrue(hexit <= 7)
        self.assertTrue(hexit < 8)

    def test_compare_str(self):
        '''Test str comparisons'''
        hexit = ehex('7')
        self.assertTrue(hexit == '7')
        self.assertTrue(hexit >= '7')
        self.assertTrue(hexit > '6')
        self.assertTrue(hexit <= '7')
        self.assertTrue(hexit < '8')

    def test_compare_ehex(self):
        '''Test ehex comparisons'''
        hexit1 = ehex(7)
        hexit2 = ehex(7)
        hexit_lt = ehex(8)
        hexit_gt = ehex(6)
        self.assertTrue(hexit1 == hexit2)
        self.assertTrue(hexit1 >= hexit2)
        self.assertTrue(hexit1 <= hexit2)
        self.assertTrue(hexit1 < hexit_lt)
        self.assertTrue(hexit1 > hexit_gt)

    def test_compare_int_hex(self):
        '''Test str-int comparisons'''
        hexit = ehex(7)
        self.assertTrue(hexit == '7')
        self.assertTrue(hexit >= '7')
        self.assertTrue(hexit > '6')
        self.assertTrue(hexit <= '7')
        self.assertTrue(hexit < '8')

        hexit = ehex('7')
        self.assertTrue(hexit == 7)
        self.assertTrue(hexit >= 7)
        self.assertTrue(hexit > 6)
        self.assertTrue(hexit <= 7)
        self.assertTrue(hexit < 8)


class TestEHexAddition(unittest.TestCase):
    '''eHex addition unit tests'''
    def test_valid_addition(self):
        '''Test valid addition'''
        self.assertTrue(ehex(3) + 3 == 6)
        self.assertTrue(ehex(3) + '3' == 6)
        self.assertTrue(ehex(3) + ehex(4) == 7)

    def test_addition_result_type(self):
        '''Test addition returns ehex'''
        if VERSION_INFO >= '2.7':
            self.assertIsInstance(ehex(3) + 3, ehex)
            self.assertIsInstance(ehex(3) + '3', ehex)
            self.assertIsInstance(ehex(3) + ehex(3), ehex)
        else:
            self.assertTrue(isinstance(ehex(3) + 3, ehex))
            self.assertTrue(isinstance(ehex(3) + '3', ehex))
            self.assertTrue(isinstance(ehex(3) + 3, ehex))

    def test_invalid_addition(self):
        '''Test out of bounds addition raises ValueError'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(ValueError):
                dummy = ehex(3) + 99
                dummy = ehex('Y') + 99
                dummy = ehex('Y') + ehex('Y')
                del dummy
        else:
            self.assertRaises(ValueError, lambda: ehex(3) + 99)
            self.assertRaises(ValueError, lambda: ehex('Y') + 99)
            self.assertRaises(ValueError, lambda: ehex('Y') + ehex('Y'))


class TestEHexSubtraction(unittest.TestCase):
    '''eHex subtraction unit tests'''
    def test_valid_subtraction(self):
        '''Test valid subtraction'''
        self.assertTrue(ehex(8) - 5 == 3)
        self.assertTrue(ehex(8) - '5' == 3)
        self.assertTrue(ehex(8) - ehex(3) == 5)

    def test_subtraction_result_type(self):
        '''Test subtraction returns ehex'''
        if VERSION_INFO >= '2.7':
            self.assertIsInstance(ehex(8) - 3, ehex)
            self.assertIsInstance(ehex(8) - '3', ehex)
            self.assertIsInstance(ehex(8) - ehex(3), ehex)
        else:
            self.assertTrue(isinstance(ehex(8) - 3, ehex))
            self.assertTrue(isinstance(ehex(8) - '3', ehex))
            self.assertTrue(isinstance(ehex(8) - ehex(3), ehex))

    def test_invalid_subtraction(self):
        '''Test out of bounds subtraction raises ValueError'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(ValueError):
                dummy = ehex(3) - 99
                dummy = ehex('A') - 99
                dummy = ehex(1) - ehex('Y')
                del dummy
        else:
            self.assertRaises(ValueError, lambda: ehex(3) - 99)
            self.assertRaises(ValueError, lambda: ehex('A') - 99)
            self.assertRaises(ValueError, lambda: ehex(1) - ehex('Y'))


class TestEHexRsubtraction(unittest.TestCase):
    '''eHex subtraction unit tests'''
    def test_valid_rsubtraction(self):
        '''Test valid rsubtraction'''
        self.assertTrue(11 - ehex(8) == 3)
        self.assertTrue('B' - ehex(8) == 3)

    def test_rsubtraction_result_type(self):
        '''Test rsubtraction returns ehex'''
        if VERSION_INFO >= '2.7':
            self.assertIsInstance(11 - ehex(8), ehex)
            self.assertIsInstance('B' - ehex(8), ehex)
        else:
            self.assertTrue(isinstance(11 - ehex(8), ehex))
            self.assertTrue(isinstance('B' - ehex(8), ehex))

    def test_invalid_rsubtraction(self):
        '''Test out of bounds rsubtraction raises ValueError'''
        if VERSION_INFO >= '2.7':
            with self.assertRaises(ValueError):
                dummy = 1 - ehex(8)
                dummy = 1 - ehex('A')
                del dummy
        else:
            self.assertRaises(ValueError, lambda: 1 - ehex(8))
            self.assertRaises(ValueError, lambda: 1 - ehex('A'))
