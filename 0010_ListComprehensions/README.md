# 0010: [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem "https://www.hackerrank.com/challenges/list-comprehensions/problem")
- level: Easy
- language: Python3


## Description of the problem
Let's learn about list comprehensions!<br>
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.<br>
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i+j+k is not equal to n.<br>
Here, 0≦i≦x; 0≦j≦y; 0≦k≦z.<br>
Please use list comprehensions rather than multiple loops, as a learning exercise.

### Example
> x=1<br>
> y=1<br>
> z=2<br>
> n=3

All permutations of [i, j, k] are:<br>
[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2].<br><br>

Print an array of the elements that do not sum to n=3.<br>
[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2].


### Input Format
Four integers x, y, z and n, each on a separate line.

### Constraints
Print the list in lexicographic increasing order.

### Sample Input 0
> 1<br>
> 1<br>
> 1<br>
> 2

### Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

### Explanation 0
Each variable x, y and z will have values of 0 or 1.<br>
All permutations of lists in the form<br>
[i, j, k] = [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1].<br><br>

Remove all arrays that sum to n=2 to leave only the valid permutations.

### Sample Input 1
> 2<br>
> 2<br>
> 2<br>
> 2

### Sample Output 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]