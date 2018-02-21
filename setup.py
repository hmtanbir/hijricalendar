# -*- coding: utf-8 -*-
from setuptools import setup
import io


def readme():
    with io.open('README.md', encoding='utf8', errors='ignore') as f:
        return f.read()


setup(name='hijricalendar',
      version='0.0.1',
      description='Hijri Calendar is a package for Bangla language users with various functionalities including Arabic date in bangla and english format',
      long_description=readme(),
      install_requires=['bangla', 'umalqurra'],
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='arabic calendar hijri calendar',
      url='https://github.com/hmtanbir/hijricalendar',
      author='Hasan Mohammad Tanbir',
      author_email='tanbir2025@gmail.com',
      license='MIT',
      packages=['hijricalendar'],
      include_package_data=True,
      zip_safe=False
      )
