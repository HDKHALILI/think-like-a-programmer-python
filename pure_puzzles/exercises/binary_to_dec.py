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
    number = number * 10 + int(char_str)
  char_str = sys.stdin.read(1)

num_str = str(number)
position = len(num_str) - 1
decimal = 0
for digit in num_str:
  decimal += (2**position) * int(digit)
  position -= 1

print(decimal)
