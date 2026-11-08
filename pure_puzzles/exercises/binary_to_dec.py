import sys

# incase the input is piped in we don't display the prompt
if sys.stdin.isatty():
  print(
    "Enter a binary number to convert to decimal: ",
    end="", flush=True
  )

char_str = sys.stdin.read(1)
number = 0

while char_str not in ("\n", "\r", ""):
  if char_str.isdigit() and char_str in ("1", "0"):
    number = number * 2 + int(char_str)
  char_str = sys.stdin.read(1)

print(number)
