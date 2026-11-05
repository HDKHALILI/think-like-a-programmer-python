import sys

print("Enter a decimal number to convert to hexadecimal: ", end="", flush=True)

hexadecimal = ''
char_str = sys.stdin.read(1)
number =  0
hex_base = 16

while char_str not in ("\n", "\r", ""):
  if char_str.isdigit():
    number = number * 10 + int(char_str)
  char_str = sys.stdin.read(1)

while number > 0:
  remainder = number % hex_base

  if remainder >= 10:
    hexadecimal = chr((remainder - 10) + ord("A")) + hexadecimal
  else:
    hexadecimal = str(remainder) + hexadecimal

  number = number // hex_base

print(f"Hexadecimal: {hexadecimal}") 
