# 0023: [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem "https://www.hackerrank.com/challenges/designer-door-mat/problem")
- level: Easy
- language: Python3

## Description of the problem
Mr. Vincent works in a door mat manufacturing company.<br>
One day, he designed a new door mat with the following specifications:

- Mat size must be *N*×*M*. (*N* is an odd natural number, and *M* is 3 times *N*.)
- The design should have 'WELCOME' written in the center.
- The design pattern should only use |, . and - characters.

### Sample Designs
>Size: 7 x 21 <br>
>---------.|.---------<br>
>------.|..|..|.------<br>
>---.|..|..|..|..|.---<br>
>-------WELCOME-------<br>
>---.|..|..|..|..|.---<br>
>------.|..|..|.------<br>
>---------.|.---------<br>
><br>
>Size: 11 x 33<br>
>---------------.|.---------------<br>
>------------.|..|..|.------------<br>
>---------.|..|..|..|..|.---------<br>
>------.|..|..|..|..|..|..|.------<br>
>---.|..|..|..|..|..|..|..|..|.---<br>
>-------------WELCOME-------------<br>
>---.|..|..|..|..|..|..|..|..|.---<br>
>------.|..|..|..|..|..|..|.------<br>
>---------.|..|..|..|..|.---------<br>
>------------.|..|..|.------------<br>
>---------------.|.---------------

### Input Format
A single line containing the space separated values of *N* and *M*.

### Constraints
- 5＜*N*＜101
- 15＜*M*＜303

### Output Format
Output the design pattern.

### Sample Input
> 9 27

### Sample Output
> ------------.|.------------<br>
> ---------.|..|..|.---------<br>
> ------.|..|..|..|..|.------<br>
> ---.|..|..|..|..|..|..|.---<br>
> ----------WELCOME----------<br>
> ---.|..|..|..|..|..|..|.---<br>
> ------.|..|..|..|..|.------<br>
> ---------.|..|..|.---------<br>
> ------------.|.------------