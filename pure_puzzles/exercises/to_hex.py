import sys

print("Enter a decimal number to convert to hexadecimal: ", end="", flush=True)

hex = ''
char_str = sys.stdin.read(1)
number =  0

while char_str not in ("\n", "\r", ""):
  if char_str.isdigit():
    number = number * 10 + int(char_str)
  char_str = sys.stdin.read(1)

while number > 0:
  remainder = number % 16

  if remainder >= 10:
    hex = chr((remainder % 10) + ord("A")) + hex
  else:
    hex = str(remainder) + hex

  number = number // 16

print(f"Hexadecimal: {hex}") 