# 0019: [Find a string](https://www.hackerrank.com/challenges/find-a-string/problem "https://www.hackerrank.com/challenges/find-a-string/problem")
- level: Easy
- language: Python3


## Description of the problem
In this challenge, the user enters a string and a substring.<br>
You have to print the number of times that the substring occurs in the given string.<br>
String traversal will take place from left to right, not from right to left.<br><br>

NOTE: String letters are case-sensitive.

### Input Format
The first line of input contains the original string.<br>
The next line contains the substring.

### Constraints
1≦len(string)≦200<br>
Each character in the string is an ascii character.

### Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

### Sample Input 0
> ABCDCDC
> CDC

### Sample Output 0
> 2

### Concept
There are a couple of new concepts:<br>
In Python, the length of a string is found by the function len(s), where s is the string.<br>
To traverse through the length of a string, use a for loop:

> for i in range(0, len(s)):<br>
>     print (s[i])

A range function is used to loop over some length:

> range (0, 5)

Here, the range loops over 0 to 4.<br>
5 is excluded.

### Constraints
-