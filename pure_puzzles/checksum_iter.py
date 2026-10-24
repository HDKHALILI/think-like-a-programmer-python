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

user_input = input("Enter a number: ").strip() + "\n"
cin = iter(user_input)
number_string = next(cin)

while number_string != "\n":
  digit = int(number_string)

  if position % 2 == 0:
    odd_length_checksum += double_digit_value(digit)
    even_length_checksum += digit
  else:
    odd_length_checksum += digit
    even_length_checksum += double_digit_value(digit)

  number_string = next(cin)
  position += 1

if (position - 1) % 2 == 0:
  checksum = even_length_checksum
else:
  checksum = odd_length_checksum

print(f"Checksum is {checksum}.")

if checksum % 10 == 0:
  print("Checksum is divisible by 10. Valid.")
else:
  print("Checksum is not divisible by 10. Invalid.")
