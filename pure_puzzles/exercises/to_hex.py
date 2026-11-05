import sys

# incase the input is piped in we don't display the prompt
if sys.stdin.isatty():
  print(
    "Enter a decimal number to convert to hexadecimal: ",
    end="", flush=True
  )

HEX_DIGITS = "0123456789ABCDEF"
hexadecimal = ''
char_str = sys.stdin.read(1)
number = 0
hex_base = 16

while char_str not in ("\n", "\r", ""):
  if char_str.isdigit():
    number = number * 10 + int(char_str)
  char_str = sys.stdin.read(1)

while number > 0:
  remainder = number % hex_base
  hexadecimal = HEX_DIGITS[remainder] + hexadecimal
  number = number // hex_base

print(f"Hexadecimal: {hexadecimal}") 