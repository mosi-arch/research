## Learning how to create an algorithm and how to work.

An algorithm for creating a new week system based on a different number of days:

1. Determine the number of days in your new week system. This can be any number, but for the purposes of this algorithm, we'll use an example of a 9-day week system.

2. Divide the number of days in your new week system by 7 to determine the number of full weeks in your system. In our example, 9 ÷ 7 = 1 with a remainder of 2, so our new week system will have one full week and an additional 2 days.

3. Decide on the names for your new days of the week. Since we have 9 days in our example, we'll need to come up with 9 unique names. These could be anything you like, such as "Sun", "Moon", "Star", "Sky", "Earth", "Water", "Fire", "Wind", and "Tree".

4. Create a mapping of your new days of the week to the traditional 7-day week. For example:

   - "Sun" maps to Sunday
   - "Moon" maps to Monday
   - "Star" maps to Tuesday
   - "Sky" maps to Wednesday
   - "Earth" maps to Thursday
   - "Water" maps to Friday
   - "Fire" maps to Saturday
   - "Wind" maps to the first day of the second week
   - "Tree" maps to the second day of the second week

5. Determine how your new week system will handle leap years. If you want your new week system to stay synchronized with the Gregorian calendar, you may need to add an extra day to your system in leap years.

6. Implement your new week system into any relevant calendars, schedules, or systems.

---

### Example calendar for a 9-day week system:

The week days of a month in a 9-day week system with 5 weeks per month:

| Week | Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday |  x day   |  y day   |
|------|--------|--------|---------|-----------|----------|--------|----------|----------|----------|
| 1    | Day 1  | Day 2  | Day 3   | Day 4     | Day 5    | Day 6  | Day 7    | Day 8    | Day 9    |
| 2    | Day 10 | Day 11 | Day 12  | Day 13    | Day 14   | Day 15 | Day 16   | Day 17   | Day 18   |
| .    | ...... | ...... | ......  | ......    | ......   | ...... | ......   | ......   | ......   |
| 5    | Day 37 | Day 38 | Day 39  | Day 40    | Day 41   | Day 42 | Day 43   | Day 44   | Day 45   |

Our weeks have 9 days, so we can use custom days for this system, or use the old system. At all this is just an example.

The calendar shows 5 weeks, but in a full year, there would be approximately 46 weeks in this system (depending on leap years and any adjustments made to keep the system synchronized with the Gregorian calendar).

---

### Calculate the calender:

In a 9-day week system, a year would have approximately 46 weeks and 1 day (or 2 days in a leap year). 

To calculate this, we can use the following formula:

```js
number of weeks = (number of days in year) / (number of days in week)
```

In the Gregorian (KHAYAM) calendar, a non-leap year has 365 days, so in a 9-day week system, the number of weeks would be:

```js
number of weeks = 365 / 9 ≈ 40.56
```

Since we cannot have a fraction of a week, we need to round this number down to the nearest integer to get the number of full weeks in a year. This gives us:

```js
number of full weeks = 40
```

To calculate the remaining days, we can subtract the number of full weeks multiplied by the number of days in a week from the total number of days in the year:

```js
remaining days = 365 - (40 * 9) = 365 - 360 = 5
```

Therefore, a year in a 9-day week system would have 46 weeks and 1 day, since the remaining 5 days cannot make up a full week. In a leap year with 366 days, there would be 46 weeks and 2 days.

---

### Schematic

Algorithm of the corresponding mathematics for a 9-day week system with 8 months per year, 2 months per season, and 5 or 6 free days at the end of the year for holidays:

1. Define the length of a week as 9 days.
2. Define the length of a month as 5 weeks, or 45 days.
3. Define the length of a season as 2 months, or 90 days.
4. Define the length of a year as 4 seasons, or 360 days.
5. Add 5 free days to the end of each year, or 6 free days in a leap year.
6. Use the free days for holidays or other special occasions.

Mathematically, we can represent this as follows:

- Number of weeks in a year: 	46 (360 days / 9 days per week)
- Number of days per month: 	45 (5 weeks x 9 days per week)
- Number of days per season: 	90 (2 months x 45 days per month)
- Number of months per year: 	8 (4 seasons x 2 months per season)
- Number of days in a year: 	365 (360 days + 5 free days) or 366 (360 days + 6 free days) in a leap year
- Number of free days per year: 5 days or 6 days in a leap year

To schedule holidays or specialoccasions using the free days, we can simply add them to the end of the year and distribute them as needed. For example, if there are 5 free days, we could allocate 2 days for a winter holiday, 2 days for a summer holiday, and 1 day for a spring or fall holiday. If there are 6 free days in a leap year, we could allocate an extra day to each holiday.

Something like this:

- Winter holiday: 	December 25th-26th (2 days)
- Spring holiday: 	March 21st (1 day)
- Summer holiday: 	July 4th-5th (2 days)
- Fall holiday: 	October 31st (1 day)
> this st-th location on normal calender we use. this example for realize and imagination.

With this schedule, the free days would be used for holidays that are evenly spaced throughout the year.

Possible example month names for the 8-month system described in the algorithm:

1. Winter I: 	December (45 days)
2. Winter II: 	January (45 days)
3. Spring I: 	February (45 days)
4. Spring II: 	March (45 days)
5. Summer I: 	April (45 days)
6. Summer II: 	May (45 days)
7. Fall I: 		September (45 days)
8. Fall II: 	October (45 days)

> June, July, August, and November are not included in this system.

At the end, this algorithm and mathematics provide a simple and consistent way to divide the year into 4 seasons with 8 months, each consisting of 2 months of 5 weeks each. The additional free days at the end of each year can be used for holidays or other special occasions, making it a flexible and customizable system. (holydays not use in the week days and will be free)

