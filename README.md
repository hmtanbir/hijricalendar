# HIJRI CALENDAR

[![Build Status](https://travis-ci.org/hmtanbir/hijricalendar.svg?branch=master)](https://travis-ci.org/hmtanbir/hijricalendar)
[![Version](https://img.shields.io/pypi/v/hijricalendar.svg?)](http://badge.fury.io/py/hijricalendar)
[![Python](https://img.shields.io/pypi/pyversions/hijricalendar.svg?)](https://pypi.python.org/pypi/hijricalendar/0.0.1)
[![Size](https://img.shields.io/github/size/hmtanbir/hijricalendar/hijricalendar/__init__.py.svg?)](https://github.com/hmtanbir/hijricalendar/)
[![codecov](https://codecov.io/gh/hmtanbir/hijricalendar/branch/master/graph/badge.svg)](https://codecov.io/gh/hmtanbir/hijricalendar)

Hijri Calendar is a package for Bangla language users with various functionalities including Arabic date in bangla and english format.

It can be used to get Arabic date that includes year, month, date, weekday in Bangla language and 
English language.

Furthermore, It can be used in global wide. Day difference between
arabic country and south asia country is considered in this module. 

This software can be used on Linux/Unix, Mac OS and Windows systems.

# Features


Get Bangla date that includes:

   - Bangla Hijri Date (১-৩০)

   - Bangla Hijri Month ('মহরম','সফর','রবিউল আউয়াল','রবিউস সানি','জুমাদিউল আউয়াল','জুমাদিউস সানি','রজব','শাবান','রমজান','শাওয়াল','জিলক্বাদ','জিলহাজ্জ্ব')

   - Bangla Hijri Year (১৪৩৯ - )
   
   - English Hijri Date (1-30)

   - English Hijri Month ('Muharram', 'Safar', 'Rabi-ul-Awwal', 'Rabi-us-Sani', 'Jamadi-ul-Awwal', 'Jamadi-us-Sani', 'Rajab', 'Shaban', 'Ramadan', 'Shawwal','Jil-Quadah', 'Jil-Hajjah',)

   - English Hijri Year (1439 - )    



 Installation


We recommend install ``hijricalendar``  through pip install using Python 3 but it supports
python 2.7


 ```
 $ sudo pip install hijricalendar
 ```

# Example
Open python shell:

```
$ python
```
Output:
```
Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>

```


To get today's date in Bangla Hijri calendar:

```
$ import hijricalendar
 
$ bangla_date = get_date()

$ print bangla_date
```

``Output: {'date': '৪', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}``

```
$ date = bangla_date['date']

$ year = bangla_date['year']

$ weekday = bangla_date['weekday']

$ month = bangla_date['month']

$ print date, year, weekday, month
```
 
``Output:   ৪ ১৪৩৯ বুধবার ৬``

To get today's date in English Hijri calendar:

``` 
 $ en_date = get_date(en=True)
 $ print en_date
```

``Output:   {'date': 4, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}``

```
 $ date = en_date['date']
 
 $ year = en_date['year']
 
 $ weekday = en_date['weekday']
 
 $ month = en_date['month']
 
 $ print date, year, weekday, month
```

``Output:   4 1439 Wednesday 6``

To get today's date in Bangla Hijri calendar in arabic timezone:

```
$ import hijricalendar
 
$ bangla_date = get_date(arabic=True)

$ print bangla_date
```

``Output: {'date': '৫', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}``

```
$ date = bangla_date['date']

$ year = bangla_date['year']

$ weekday = bangla_date['weekday']

$ month = bangla_date['month']

$ print date, year, weekday, month
```
 
``Output:  ৫  ১৪৩৯ বুধবার ৬``

To get today's date in English Hijri calendar in arabic timezone:

``` 
 $ en_date = get_date(en=True)
 $ print en_date
```

``Output:   {'date': 5, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}``

```
 $ date = en_date['date']
 
 $ year = en_date['year']
 
 $ weekday = en_date['weekday']
 
 $ month = en_date['month']
 
 $ print date, year, weekday, month
```

``Output:   5 1439 Wednesday 6``

To get specific date in Bangla Hijri calendar:

```
# format: get_date(date, month, year)
 
$ bangla_date = get_date(21, 2, 2018)

$ print bangla_date
```

``Output: {'date': '৪', 'year': '১৪৩৯', 'weekday': 'বুধবার', 'month': '৬'}``

```
$ date = bangla_date['date']

$ year = bangla_date['year']

$ weekday = bangla_date['weekday']

$ month = bangla_date['month']

$ print date, year, weekday, month
```
 
``Output:   ৪ ১৪৩৯ বুধবার ৬``

To get specific date in English Hijri calendar:

```
 # format: get_date(date, month, year, en=True)
 $ en_date = get_date(21, 2, 2018, en=True)
 $ print en_date
```

``Output:   {'date': 4, 'year': 1439, 'weekday': 'Wednesday', 'month': 6}``

```
 $ date = en_date['date']
 
 $ year = en_date['year']
 
 $ weekday = en_date['weekday']
 
 $ month = en_date['month']
 
 $ print date, year, weekday, month
```

``Output:   4 1439 Wednesday 6``

# Contribute


Create Github Pull Request https://github.com/hmtanbir/hijricalendar/pulls


If you have suggestion use GitHub issue system or send a message in linkedin https://www.linkedin.com/in/hmtanbir.

[![Build Status](https://travis-ci.org/hmtanbir/hijricalendar.svg?branch=master)](https://travis-ci.org/hmtanbir/hijricalendar)