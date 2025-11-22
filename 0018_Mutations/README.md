# 0018: [Mutations](https://www.hackerrank.com/challenges/python-mutations/problem "https://www.hackerrank.com/challenges/python-mutations/problem")
- level: Easy
- language: Python3


## Description of the problem
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).<br>
Let's try to understand this with an example.<br>
You are given an immutable string, and you want to make changes to it.

### Example
> >>> string = "abracadabra"

You can access an index by:

> >>> print string[5]<br>
> a

What if you would like to assign a value?

> >>> string[5] = 'k' <br>
> Traceback (most recent call last):<br>
>   File "<stdin>", line 1, in <module><br>
> TypeError: 'str' object does not support item assignment

How would you approach this?

- One solution is to convert the string to a list and then change the value.

### Example

> >>> string = "abracadabra"<br>
> >>> l = list(string)<br>
> >>> l[5] = 'k'<br>
> >>> string = ''.join(l)<br>
> >>> print string<br>
> abrackdabra

- Another approach is to slice the string and join it back.

### Example

> >>> string = string[:5] + "k" + string[6:]<br>
> >>> print string<br>
> abrackdabra<br>

### Task
Read a given string, change the character at a given index and then print the modified string.

### Function Description
Complete the mutate_string function in the editor below.<br>
mutate_string has the following parameters:

- string string: the string to change
- int position: the index to insert the character at
- string character: the character to insert

### Returns
- string: the altered string


### Input Format
The first line contains a string, string.<br>
The next line contains an integer position, the index location and a string character, separated by a space.

### Sample Input 0
> STDIN           Function<br>
> -----           --------<br>
> abracadabra     s = 'abracadabra'<br>
> 5 k             position = 5, character = 'k'

### Sample Output 0
> abrackdabra