#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stephan Wallentin on 2011-06-12.
Copyright (c) 2011 stephan.wallentin@gmail.com. All rights reserved.
"""

import sys
import os
import datetime


def main():
	date = datetime.date(2011, 4, 28)
	delta = datetime.timedelta(days=60)
	print date+delta


if __name__ == '__main__':
	main()

