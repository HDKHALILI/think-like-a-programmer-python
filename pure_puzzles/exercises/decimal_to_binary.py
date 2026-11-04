import sys

print("Enter a number to convert to binary: ", end="", flush=True)

binary = ''
char_str = sys.stdin.read(1)
number =  0

while char_str not in ("\n", "\r", ""):
  if char_str.isdigit():
    number = number * 10 + int(char_str)
  char_str = sys.stdin.read(1)

while number > 0:
  binary = str(number % 2) + binary  
  number = number // 2

print(f"Binary: {binary}")


