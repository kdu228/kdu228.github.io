# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:36:29 2025

@author: kdu22
"""
import pytz
import datetime
from pyscript import document
from datetime import datetime as dt


def format_date(dt_, fmt="%H : %M : %S"):
    return dt_.strftime(fmt)


def now(fmt="%H : %M : %S"):
    return format_date(dt.now(), fmt)


def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)
