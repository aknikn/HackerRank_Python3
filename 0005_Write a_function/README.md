# 0005: [Write a function](https://www.hackerrank.com/challenges/write-a-function/problem "https://www.hackerrank.com/challenges/write-a-function/problem")
- level: Medium
- language: Python3


## Description of the problem
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day.<br>
It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.<br>
A leap year contains a leap day.<br><br>

In the Gregorian calendar, three conditions are used to identify leap years:
- The year can be evenly divided by 4, is a leap year, unless:
	- The year can be evenly divided by 100, it is NOT a leap year, unless:
		- The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

### Task
Given a year, determine whether it is a leap year.<br>
If it is a leap year, return the Boolean True, otherwise return False.<br><br>

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.<br>
It is only necessary to complete the is_leap function.

### Input Format
Read year, the year to test.

### Constraints
1990≦year≦10^5

### Output Format
The function must return a Boolean value (True/False).<br>
Output is handled by the provided code stub.

### Sample Input 0
> 1990

### Sample Output 0
> False


### Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.