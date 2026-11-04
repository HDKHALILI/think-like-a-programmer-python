# Chapter 02: Pure Puzzles

Descriptions of what problem each file is solving

### Problems

##### 1\. Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like half of a perfect 5 × 5 square (or a right triangle):

[`half_square.py`](half_square.py)

```
#####
####
###
##
#
```

##### 2\. Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like a sideways triangle:

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

##### 3\. Luhn Checksum Validation

The Luhn formula is a widely used system for validating identification numbers. Using the original number, double the value of every other digit. Then add the values of the individual digits together (if a doubled value now has two digits, add the digits individually). The identification number is valid if the sum is divisible by 10.

Write a program that takes an identification number of arbitrary length and determines whether the number is valid under the Luhn formula. The program must process each character before reading the next one.

For an added challenge we will double every other digit, starting from the right most digit of the original number.

[`checksum_iter.py`](checksum_iter.py) I have used `iter()` to emulate the C++'s `cin.get()`. This solution do maintain the flow of the C++ version of the program but doesn't really honour the constraint of processing each character before reading the next one. I have added character validation to ignore non digit characters.

[`checksum.py`](checksum.py) I have updated the [`checksum_iter.py`](checksum_iter.py) to use `sys.stdin.read(1)` to make sure the program satisfies the constraint of processing each character before reading the next one.

##### 3\. Decode a Message

A message has been encoded as a text stream that is to be read character by character. The stream contains a series of comma-delimited integers, each a positive number capable of being represented by a C++ int. However, the character represented by a particular integer depends on the current decoding mode. There are three modes: uppercase, lowercase, and punctuation.

In uppercase mode, each integer represents an uppercase letter: The integer modulo 27 indicates the letter of the alphabet (where 1 = A and so on). So an input value of 143 in uppercase mode would yield the letter H because 143 modulo 27 is 8 and H is the eighth letter in the alphabet.

The lowercase mode works the same but with lowercase letters; the remainder of dividing the integer by 27 represents the lowercase letter (1 = a and so on). So an input value of 56 in lowercase mode would yield the letter b because 57 modulo 27 is 2 and b is the second letter in the alphabet.

In punctuation mode, the integer is instead considered modulo 9. So 19 would yield an exclamation point because 19 modulo 9 is 1.

At the beginning of each message, the decoding mode is uppercase letters. Each time the modulo operation (by 27 or 9, depending on mode) results in 0, the decoding mode switches. If the current mode is uppercase, the mode switches to lowercase letters. If the current mode is lowercase, the mode switches to punctuation, and if it is punctuation, it switches back to uppercase.

[`decode_message.py`](decode_message.py) As a bonus I have added input validation, it will discard none digit characters. The correct input is always a series of comma separated numbers.

### Exercises

##### 1\. Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:

[`exercises/inverted_pyramid.py`](exercises/inverted_pyramid.py)

```
########
 ######
  ####
   ##
```

##### 2\. Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:

[`exercises/diamond.py`](exercises/diamond.py)

```
   ##
  ####
 ######
########
########
 ######
  ####
   ##
```

##### 3\. Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:

[`exercises/x_shape.py`](exercises/x_shape.py)

```
#            #
 ##        ##
  ###    ###
   ########
   ########
  ###    ###
 ##        ##
#            #
```

##### 4\. A simple decimal to binary converter.

[`exercises/decimal_to_binary.py`](exercises/decimal_to_binary.py) We can just use the regular `input` statement to capture user's input, however, I have followed the them of the chapter where we capture each character one at a time. From here we can extend the program to process a series of numbers.
