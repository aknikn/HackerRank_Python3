# 0012: [Nested List](https://www.hackerrank.com/challenges/nested-list/problem "https://www.hackerrank.com/challenges/nested-list/problem")
- level: Easy
- language: Python3


## Description of the problem
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.<br><br>

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

### Example

> records = [["chi". 20.0], ["beta". 50.0], ["alpha". 50.0]]

The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0.<br>
There are two students with that score: ["beta", "alpha"].<br>
Ordered alphabetically, the names are printed as:

> "alpha"<br>
> "beta"

### Input Format
The first line contains an integer, N, the number of students.<br>
The 2N subsequent lines describe each student over 2 lines.<br>
- The first line contains a student's name.
- The second line contains their grade.

### Constraints
- 2≦N≦5
- There will always be one or more students having the second lowest grade.

### Output Format
Print the name(s) of any student(s) having the second lowest grade in.<br>
If there are multiple students, order their names alphabetically and print each one on a new line.

### Sample Input 0
> 5<br>
> Harry<br>
> 37.21<br>
> Berry<br>
> 37.21<br>
> Tina<br>
> 37.2<br>
> Akriti<br>
> 41<br>
> Harsh<br>
> 39

### Sample Output 0
> Berry<br>
> Harry

### Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

> python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina.<br>
The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
