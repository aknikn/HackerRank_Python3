# 0020: [String Validators](https://www.hackerrank.com/challenges/string-validators/problem "https://www.hackerrank.com/challenges/string-validators/problem")
- level: Easy
- language: Python3


## Description of the problem
Python has built-in string validation methods for basic data.<br>
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.<br><br>

str.isalnum()<br>
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).<br>

> >>> print 'ab123'.isalnum()<br>
> True<br>
> >>> print 'ab123#'.isalnum()<br>
> False

str.isalpha()<br>
This method checks if all the characters of a string are alphabetical (a-z and A-Z).<br>

> >>> print 'abcD'.isalpha()<br>
> True<br>
> >>> print 'abcd1'.isalpha()<br>
> False

str.isdigit()<br>
This method checks if all the characters of a string are digits (0-9).<br>

> >>> print '1234'.isdigit()<br>
> True<br>
> >>> print '123edsd'.isdigit()<br>
> False

str.islower()<br>
This method checks if all the characters of a string are lowercase characters (a-z).<br>

> >>> print 'abcd123#'.islower()<br>
> True<br>
> >>> print 'Abcd123#'.islower()<br>
> False

str.isupper()<br>
This method checks if all the characters of a string are uppercase characters (A-Z).<br>

> >>> print 'ABCD123#'.isupper()<br>
> True<br>
> >>> print 'Abcd123#'.isupper()<br>
> False

### Task
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.




### Input Format
A single line containing a string S.

### Constraints
0＜len(S)＜1000

### Output Format
In the first line, print True if S has any alphanumeric characters.<br>
Otherwise, print False.<br><br>

In the second line, print True if S has any alphabetical characters.<br>
Otherwise, print False.<br><br>

In the third line, print True if S has any digits.<br>
Otherwise, print False.<br><br>

In the fourth line, print True if S has any lowercase characters.<br>
Otherwise, print False.<br><br>

In the fifth line, print True if S has any uppercase characters.<br>
Otherwise, print False.

### Sample Input 0
> qA2

### Sample Output 0
> True
> True
> True
> True
> True