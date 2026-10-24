# Chapter 02: Pure Puzzles

Descriptions of what problem each file is solving

1\. Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like half of a perfect 5 × 5 square (or a right triangle):

[`half_square.py`](half_square.py)

```
#####
####
###
##
#
```

2\. Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like a sideways triangle:

[`sideway_triangle.py`](sideway_triangle.py)

```
#
##
###
####
###
##
#
```

3\. **Luhn Checksum Validation**

The Luhn formula is a widely used system for validating identification numbers. Using the original number, double the value of every other digit. Then add the values of the individual digits together (if a doubled value now has two digits, add the digits individually). The identification number is valid if the sum is divisible by 10.

Write a program that takes an identification number of arbitrary length and determines whether the number is valid under the Luhn formula. The program must process each character before reading the next one.

For an added challenge we will double every other digit, starting from the right most digit of the original number.

[`checksum_iter.py`](checksum_iter.py) I have used `iter()` to emulate the C++'s `cin.get()`. This solution do maintain the flow of the C++ version of the program but doesn't really honour the constraint of processing each character before reading the next one.
