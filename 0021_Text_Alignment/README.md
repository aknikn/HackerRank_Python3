# 0021: [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem "https://www.hackerrank.com/challenges/text-alignment/problem")
- level: Easy
- language: Python3


## Description of the problem
In Python, a string of text can be aligned left, right and center.<br>

.ljust(width)<br>
This method returns a left aligned string of length width.

> >>> width = 20<br>
> >>> print 'HackerRank'.ljust(width,'-')<br>
> HackerRank----------  <br>

.center(width)<br>
This method returns a centered string of length width.

> >>> width = 20<br>
> >>> print 'HackerRank'.center(width,'-')<br>
> -----HackerRank-----<br>

.rjust(width)<br>
This method returns a right aligned string of length width.

> >>> width = 20<br>
> >>> print 'HackerRank'.rjust(width,'-')<br>
> ----------HackerRank


###Task
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

### Input Format
A single line containing the thickness value for the logo.

### Constraints
0＜*tickness*＜50

### Output Format
Output the desired logo.

### Sample Input
> 5

### Sample Output
>     H
>    HHH
>   HHHHH
>  HHHHHHH
> HHHHHHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHHHHHHHHHHHHHHHHHHHHHH
>   HHHHHHHHHHHHHHHHHHHHHHHHH
>   HHHHHHHHHHHHHHHHHHHHHHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>   HHHHH               HHHHH
>                     HHHHHHHHH
>                      HHHHHHH
>                       HHHHH
>                        HHH
>                         H