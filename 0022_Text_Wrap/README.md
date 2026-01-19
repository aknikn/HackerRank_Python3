# 0022: [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem "https://www.hackerrank.com/challenges/text-wrap/problem")
- level: Easy
- language: Python3


## Description of the problem
You are given a string *S* and width *W*.<br>
Your task is to wrap the string into a paragraph of width *W*.<br>

### Function Description
Complete the wrap function in the editor below.<br>
wrap has the following parameters:
- string string: a long string
- int max_width: the width to wrap to

### Returns
string: a single string with newline characters ('\n') where the breaks should be

### Input Format
The first line contains a string, *String*.<br>
The second line contains the width, *maxWidth*.

### Constraints
- 0＜*len*(*String*)＜1000
- 0＜*maxWidth*＜*len*(*String*)

### Sample Input 0
> ABCDEFGHIJKLIMNOQRSTUVWXYZ<br>
> 4

### Sample Output 0
> ABCD<br>
> EFGH<br>
> IJKL<br>
> IMNO<br>
> QRST<br>
> UVWX<br>
> YZ