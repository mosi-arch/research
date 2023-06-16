### New Hour System
The algorithm of a new time system that divides a day into 20 hours, rather than the 24 hours in the current system. Each hour in the new system is 72 minutes long, compared to 60 minutes in the current system. The minute in the new system is 48 seconds long, compared to 60 seconds in the current system. Finally, the second in the new system is 0.6 seconds long, compared to 1 second in the current system.

To convert a given time from the current system to the new system, we use the following formulas:

```js
New Hours = (Current Hours * 20) / 24
New Minutes = (Current Minutes * 90) / 60
New Seconds = (Current Seconds * 80) / 60
```

For example, to convert the time 12:30:45 in the current system to the new system, we would first calculate the new hours as:

`New Hours = (12 * 20) / 24 = 10`

Next, we would calculate the new minutes as:

`New Minutes = (30 * 90) / 60 = 45`

Finally, we would calculate the new seconds as:

`New Seconds = (45 * 80) / 60 = 60`

Note that the new seconds value is 60, which is equivalent to 1 minute in the new system.

We can also convert all 24 hours of the current system to the new system by looping through all 20 new system hours and calculating the equivalent hour in the current system:

```py
for i in range(20):
    current_hour = (i * 24) / 20
    new_hour = i
    # print current_hour and new_hour
```

Similarly, we can also convert all 60 minutes of an hour in the current system to the new system by looping through all 90 new system minutes and calculating the equivalent minute in the current system:

```py
for i in range(90):
    current_minute = (i * 60) / 90
    new_minute = i
    # print current_minute and new_minute
```

Finally, we can convert all 60 seconds of a minute in the current system to the new system by looping through all 80 new system seconds and calculating the equivalent second in the current system:

```py
for i in range(80):
    current_second = (i * 60) / 80
    new_second = i
    # print current_second and new_second
```

This algorithm provides an interesting and different approach to measuring time, with longer hours and minutes and shorter seconds. However, it is important to note that it is not currently in use and would require significant changes to be implemented in practice.\
So best usecase in the :
- "Open world games"
- "Secure connection in large organizations"
- "Detecting fraud packages on the custom nets"

#

### Example code for calculation
```py
# =====================================================
# NEW HOUR SYSTEM
# =====================================================

def convert_to_new_system(current_hours, current_minutes, current_seconds):
    # Convert to new system
    new_hours = (current_hours * 20) / 24
    new_minutes = (current_minutes * 90) / 60
    new_seconds = (current_seconds * 80) / 60
    
    # Return new system time as tuple
    return (int(new_hours), int(new_minutes), int(new_seconds))

def print_all_new_hours():
    # Loop through all 20 new system hours
    for i in range(20):
        # Convert hour to current system
        current_hour = (i * 24) / 20

        # Convert hour to new system
        new_hour = i

        # Print current and new hour
        print("Current Hour: ", current_hour)
        print("New Hour: ", new_hour)
        
def print_all_new_minutes(current_hour):
    # Loop through all 90 new system minutes
    for i in range(90):
        # Convert minute to current system
        current_minute = (i * 60) / 90

        # Convert minute to new system
        new_minute = i

        # Print current and new minute
        print("Current Time: ", current_hour, ":", int(current_minute))
        print("New Time: ", current_hour, ":", new_minute)
        
def print_all_new_seconds(current_hour, current_minute):
    # Loop through all 80 new system seconds
    for i in range(80):
        # Convert second to current system
        current_second = (i * 60) / 80

        # Convert second to new system
        new_second = i

        # Print current and new second
        print("Current Time: ", current_hour, ":", current_minute, ":", int(current_second))
        print("New Time: ", current_hour, ":", current_minute, ":", new_second)

# =====================================================
# TEST
# =====================================================

# Convert current time to new system
new_time = convert_to_new_system(12, 30, 45)
print("New Time: ", new_time)

# Print all new system hours
print_all_new_hours()

# Print all new system minutes for hour 1
print_all_new_minutes(1)

# Print all new system seconds for hour 1, minute 30
print_all_new_seconds(1, 30)
```

> this algorithm made by me in the year 2000. iran, shiraz
