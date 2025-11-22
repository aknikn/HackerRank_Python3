# 0017: [String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem "https://www.hackerrank.com/challenges/python-string-split-and-join/problem")
- level: Easy
- language: Python3


## Description of the problem
In Python, a string can be split on a delimiter.

### Example
> >>> a = "this is a string"<br>
> >>> a = a.split(" ") # a is converted to a list of strings. <br>
> >>> print a<br>
> ['this', 'is', 'a', 'string']<br><br>

Joining a string is simple:<br>
> >>> a = "-".join(a)<br>
> >>> print a<br>
> this-is-a-string

### Task
You are given a string.<br>
Split the string on a " " (space) delimiter and join using a - hyphen.

### Function Description
Complete the split_and_join function in the editor below.<br>
split_and_join has the following parameters:

- string line: a string of space-separated words

### Returns
string: the resulting string

### Input Format
The one line contains a string consisting of space separated words.

### Sample Input 0
> this is a string   

### Sample Output 0
> this-is-a-string