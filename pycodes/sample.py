# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:36:29 2025

@author: kdu22
"""
from datetime import datetime
import tzlocal # $ pip install tzlocal

now = datetime.now(tzlocal.get_localzone())
print(now.strftime('%Z'))
# -> MSK
print(now.tzname())
# -> MSK
