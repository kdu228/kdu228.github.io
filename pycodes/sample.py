# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 12:36:29 2025

@author: kdu22
"""
import pytz
import datetime
# Get the current time in UTC
utc_now = datetime.datetime.utcnow()
# Get the local timezone
local_tz = pytz.timezone('Asia/Kolkata')
# Convert the UTC time to local time
local_now = utc_now.replace(tzinfo=pytz.utc).astimezone(local_tz)
# Print the local time and timezone
print("Local time: ", local_now.strftime('%Y-%m-%d %H:%M:%S'))
print("Timezone: ", local_now.tzinfo)
