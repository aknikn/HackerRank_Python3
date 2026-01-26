# 0025: [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli/problem "https://www.hackerrank.com/challenges/alphabet-rangoli/problem")
- level: Easy
- language: Python3


## Description of the problem
You are given an integer, *N*.<br>
Your task is to print an alphabet rangoli of size *N*.<br>
(Rangoli is a form of Indian folk art based on creation of patterns.)<br><br>

Different sizes of alphabet rangoli are shown below:<br>

> #size 3<br>
> <br>
> ----c----<br>
> --c-b-c--<br>
> c-b-a-b-c<br>
> --c-b-c--<br>
> ----c----<br>
> <br>
> #size 5<br>
> <br>
> --------e--------<br>
> ------e-d-e------<br>
> ----e-d-c-d-e----<br>
> --e-d-c-b-c-d-e--<br>
> e-d-c-b-a-b-c-d-e<br>
> --e-d-c-b-c-d-e--<br>
> ----e-d-c-d-e----<br>
> ------e-d-e------<br>
> --------e--------<br>
> <br>
> #size 10<br>
> <br>
> ------------------j------------------<br>
> ----------------j-i-j----------------<br>
> --------------j-i-h-i-j--------------<br>
> ------------j-i-h-g-h-i-j------------<br>
> ----------j-i-h-g-f-g-h-i-j----------<br>
> --------j-i-h-g-f-e-f-g-h-i-j--------<br>
> ------j-i-h-g-f-e-d-e-f-g-h-i-j------<br>
> ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----<br>
> --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--<br>
> j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j<br>
> --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--<br>
> ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----<br>
> ------j-i-h-g-f-e-d-e-f-g-h-i-j------<br>
> --------j-i-h-g-f-e-f-g-h-i-j--------<br>
> ----------j-i-h-g-f-g-h-i-j----------<br>
> ------------j-i-h-g-h-i-j------------<br>
> --------------j-i-h-i-j--------------<br>
> ----------------j-i-j----------------<br>
> ------------------j------------------<br>

The center of the rangoli has the first alphabet letter a, and the boundary has the *N*th alphabet letter (in alphabetical order).

### Function Description
Complete the rangoli function in the editor below.<br>
rangoli has the following parameters:

- int size: the size of the rangoli

### Returns
- string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)



### Input Format
Only one line of input containing *size*, the size of the rangoli.

### Constraints
0＜*size*＜27

### Sample Input
> 5

### Sample Output
> --------e--------<br>
> ------e-d-e------<br>
> ----e-d-c-d-e----<br>
> --e-d-c-b-c-d-e--<br>
> e-d-c-b-a-b-c-d-e<br>
> --e-d-c-b-c-d-e--<br>
> ----e-d-c-d-e----<br>
> ------e-d-e------<br>
> --------e--------