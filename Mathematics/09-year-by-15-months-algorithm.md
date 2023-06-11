## New year system with 15 months
The algorithm for a new year system with 15 months, where 10 months have 24 days and 5 months have 25 days. If it's a leap year, then 9 months have 24 days and 6 months have 25 days:

1. Determine if it's a leap year. A leap year is any year that is evenly divisible by 4, except for years that are also divisible by 100 but not by 400. If it's a leap year, then set the number of days in 9 months to 24 and the number of days in 6 months to 25. Otherwise, set the number of days in 10 months to 24 and the number of days in 5 months to 25.

2. Visualizing a table with 15 rows, one for each month. Label the first 10 rows with the names of the 10 months that have 24 days, and label the next 5 rows with the names of the 5 months that have 25 days.

3. For each month with 24 days, assign a number from 1 to 10. For example, the first month could be assigned the number 1, the second month could be assigned the number 2, and so on.

4. For each month with 25 days, assign a number from 11 to 15. For example, the first month could be assigned the number 11, the second month could be assigned the number 12, and so on.

5. Calculate the total number of days in the year by adding up the number of days in each month.

6. **Season 1**: first four months. **Season 2**: next four months. **Season 3**: next three months. **Season 4**: last four months.

- Non-leap year:

| Month | Days | Number | Season |
|-------|------|--------|--------|
| Month1| 24   | 1      | 1      |
| Month2| 24   | 2      | 1      |
| Month3| 24   | 3      | 1      |
| Month4| 24   | 4      | 1      |
| Month5| 24   | 5      | 2      |
| Month6| 24   | 6      | 2      |
| Month7| 24   | 7      | 2      |
| Month8| 24   | 8      | 2      |
| Month9| 24   | 9      | 3      |
| Month10| 24  | 10     | 3      |
| Month11| 25  | 11     | 3      |
| Month12| 25  | 12     | 4      |
| Month13| 25  | 13     | 4      |
| Month14| 25  | 14     | 4      |
| Month15| 25  | 15     | 4      |

- Leap year:

| Month | Days | Number | Season |
|-------|------|--------|--------|
| Month1| 24   | 1      | 1      |
| Month2| 24   | 2      | 1      |
| Month3| 24   | 3      | 1      |
| Month4| 24   | 4      | 1      |
| Month5| 24   | 5      | 2      |
| Month6| 24   | 6      | 2      |
| Month7| 24   | 7      | 2      |
| Month8| 24   | 8      | 2      |
| Month9| 24   | 9      | 3      |
| Month10| 25  | 10     | 3      |
| Month11| 25  | 11     | 3      |
| Month12| 25  | 12     | 4      |
| Month13| 25  | 13     | 4      |
| Month14| 25  | 14     | 4      |
| Month15| 25  | 15     | 4      |

#

### Mathematical Formula:

1. Total number of days in a non-leap year:

```js
Total days = [10 * 24] + [5 * 25] = 365
```

2. Total number of days in a leap year:

```js
Total days = [9 * 24] + [6 * 25] = 366
```

3. Number of days in a month:

For months 1-10 (non-leap year), or months 1-9 and 11-15 (leap year):

```js
Days in month = 24
```

For months 11-15 (non-leap year), or month 10 (leap year):

```js
Days in month = 25
```

4. Assigning a number to each month:

For months 1-10 (non-leap year), or months 1-9 and 11-15 (leap year):

```js
Number = month number
```

For month 10 (non-leap year):

`Number = 10`

For month 10 (leap year):

`Number = 9`

For months 11-15 (non-leap year):

```js
Number = month number + 5
```

For months 10-15 (leap year):

```js
Number = month number + 4
```

---

> this algorithm made by me in the year 2000. iran, shiraz university
