# -*- coding: utf-8 -*-
import unittest
import os
import sys
import bangla
from umalqurra.hijri_date import HijriDate

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

import hijricalendar


class TestHijriCalendar(unittest.TestCase):
    def test_get_date(self):
        today = HijriDate.today()
        date = bangla.convert_english_digit_to_bangla_digit(int(today.day) - int(1))
        year = bangla.convert_english_digit_to_bangla_digit(int(today.year))
        month = bangla.convert_english_digit_to_bangla_digit(int(today.month))
        weekday = hijricalendar.weekdays_dict[today.day_name_en]

        result = hijricalendar.get_date()
        expect = {'date': date, 'year': year, 'weekday': weekday, 'month': month}
        self.assertEquals(result, expect)

    def test_get_date_when_en_is_true(self):
        today = HijriDate.today()
        date = int(today.day) - int(1)
        year = int(today.year)
        month = int(today.month)
        weekday = today.day_name_en

        result = hijricalendar.get_date(en=True)
        expect = {'date': date, 'year': year, 'weekday': weekday, 'month': month}
        self.assertEquals(result, expect)

    def test_get_date_with_args(self):
        result = hijricalendar.get_date(21, 2, 2018)
        expect = {'date': '৪', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}
        self.assertEquals(result, expect)

    def test_get_date_with_args_when_only_arabic_is_true(self):
        result = hijricalendar.get_date(21, 2, 2018, arabic=True)
        expect = {'date': '৫', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}
        self.assertEquals(result, expect)

    def test_get_date_with_args_when_en_is_true(self):
        result = hijricalendar.get_date(21, 2, 2018, en=True)
        expect = {'date': 4, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}
        self.assertEquals(result, expect)

    def test_get_date_with_args_when_both_en_and_arabic_is_true(self):
        result = hijricalendar.get_date(21, 2, 2018, en=True, arabic=True)
        expect = {'date': 5, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}
        self.assertEquals(result, expect)

    def test_get_month(self):
        result = hijricalendar.get_month()
        today = HijriDate.today()
        month = int(today.month)
        expect = month
        self.assertEquals(result, expect)

    def test_get_month_for_specific_date(self):
        result = hijricalendar.get_month(21, 2, 2018)
        expect = 6
        self.assertEquals(result, expect)

    def test_get_month_name(self):
        result = hijricalendar.get_month_name(21, 2, 2018)
        expect = hijricalendar.month_name_dict_bn[6]  # since arabic month =6 using get_month method
        self.assertEquals(result, expect)

    def test_get_month_name_when_en_is_true(self):
        result = hijricalendar.get_month_name(21, 2, 2018, en=True)
        expect = hijricalendar.month_name_dict_en[6]  # since arabic month =6 using get_month method
        self.assertEquals(result, expect)


if __name__ == "__main__":
    unittest.main()
