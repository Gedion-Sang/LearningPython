# Time function

import time
current_time = time.time()
print(current_time)  # time in seconds

import time
current_time =time.time()
local_time = time.ctime(current_time)
print("The local time is:",local_time) # To print the current local  time in the format: "Day, Month dd hh:mm:ss yyyy"

import time
epoch_time = 1721907572.564324
local_time = time.ctime(epoch_time)
print("The local time is:",local_time)
''' To print the local time in epoch time in the format; "Day, Month dd hh:mm:ss yyyy" 
epoch time is the number of seconds since January 1, 1970. '''