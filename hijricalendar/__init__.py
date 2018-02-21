# -*- coding: utf-8 -*-

import bangla
from umalqurra.hijri_date import HijriDate

bangla_weekdays = bangla.python_bangla_weekdays

month_name_dict_en = {
    1: 'Muharram',
    2: 'Safar',
    3: 'Rabi-ul-Awwal',
    4: 'Rabi-us-Sani',
    5: 'Jamadi-ul-Awwal',
    6: 'Jamadi-us-Sani',
    7: 'Rajab',
    8: 'Shaban',
    9: 'Ramadan',
    10: 'Shawwal',
    11: 'Jil-Quadah',
    12: 'Jil-Hajjah',
}

month_name_dict_bn = {
    1: 'মহরম',
    2: 'সফর',
    3: 'রবিউল আউয়াল',
    4: 'রবিউস সানি',
    5: 'জুমাদিউল আউয়াল',
    6: 'জুমাদিউস সানি',
    7: 'রজব',
    8: 'শাবান',
    9: 'রমজান',
    10: 'শাওয়াল',
    11: 'জিলক্বাদ',
    12: 'জিলহাজ্জ্ব',
}

weekdays_dict = {
    'Monday': bangla_weekdays[0],
    'Tuesday': bangla_weekdays[1],
    'Wednesday': bangla_weekdays[2],
    'Thursday': bangla_weekdays[3],
    'Friday': bangla_weekdays[4],
    'Saturday': bangla_weekdays[5],
    'Sunday': bangla_weekdays[6],
}


# Hijri date in bangla format
# Example: $ bangla_date = get_date()
#          $ print bangla_date
#
# Output: {'date': '৪', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}
#
#           $ date = bangla_date['date']
#           $ year = bangla_date['year']
#           $ weekday = bangla_date['weekday']
#           $ month = bangla_date['month']
#           $ print date, year, weekday, month
#
# Output:   ৪ ১৪৩৯ বুধবার ৬

# Example: $ en_date = get_date(en=True)
#          $ print en_date
#
# Output:   {'date': 4, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}
#
#           $ date = en_date['date']
#           $ year = en_date['year']
#           $ weekday = en_date['weekday']
#           $ month = en_date['month']
#           $ print date, year, weekday, month
#
# Output:   4 1439 Wednesday 6


def get_date(passed_date=None, passed_month=None, passed_year=None, en=False, arabic=False):
    if passed_date == None and passed_month == None and passed_year == None:
        current_date_object = HijriDate.today()
    else:
        current_date_object = HijriDate(passed_year, passed_month, passed_date, gr=True)

    passed_year = int(current_date_object.year)
    passed_month = int(current_date_object.month)

    if arabic == 1:
        passed_date = int(current_date_object.day)
    else:
        passed_date = int(current_date_object.day) - int(1)

    passed_week = current_date_object.day_name_en

    hijri_date_month_year_bn = {
        'date': bangla.convert_english_digit_to_bangla_digit(passed_date),
        'month': bangla.convert_english_digit_to_bangla_digit(passed_month),
        'year': bangla.convert_english_digit_to_bangla_digit(passed_year),
        'weekday': weekdays_dict[passed_week],
    }

    hijri_date_month_year_en = {
        'date': passed_date,
        'month': passed_month,
        'year': passed_year,
        'weekday': passed_week,
    }

    if en == 1:
        return hijri_date_month_year_en
    else:
        return hijri_date_month_year_bn


# return month number in integer format
# $ print get_month()
# output: 6


def get_month(passed_date=None, passed_month=None, passed_year=None):
    if passed_date == None and passed_month == None and passed_year == None:
        current_date_object = HijriDate.today()
    else:
        current_date_object = HijriDate(passed_year, passed_month, passed_date, gr=True)

    return int(current_date_object.month)


# return month name in bangla format
# $ print get_month_name()
# output: জুমাদিউস সানি

# return month name in english format
# $ print get_month_name(en=True)
# output: Jamadi-us-Sani


def get_month_name(passed_date=None, passed_month=None, passed_year=None, en=False):
    month = get_month(passed_date, passed_month, passed_year)

    if en == 1:
        return month_name_dict_en[month]
    else:
        return month_name_dict_bn[month]
