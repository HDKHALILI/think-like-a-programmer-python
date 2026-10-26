import sys

def double_digit_value(digit):
  doubled_digit = digit * 2
  sum = 0
  if doubled_digit >= 10:
    sum = 1 + (doubled_digit % 10)
  else:
    sum = doubled_digit

  return sum

checksum = 0
odd_length_checksum = 0
even_length_checksum = 0
position = 1

print("Enter a number: ", end="", flush=True)
number_string = sys.stdin.read(1)

while number_string not in ("\n", "\r"):
  if number_string.isdigit():
    digit = int(number_string)

    if position % 2 == 0:
      odd_length_checksum += double_digit_value(digit)
      even_length_checksum += digit
    else:
      odd_length_checksum += digit
      even_length_checksum += double_digit_value(digit)

    position += 1

  number_string = sys.stdin.read(1)

# subtract 1 from position because the last char is EOL
if (position - 1) % 2 == 0:
  checksum = even_length_checksum
else:
  checksum = odd_length_checksum

print(f"Checksum is {checksum}.")

if checksum % 10 == 0:
  print("Checksum is divisible by 10. Valid.")
else:
  print("Checksum is not divisible by 10. Invalid.")
