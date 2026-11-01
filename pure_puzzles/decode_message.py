import sys

mode = "UPPERCASE"
output_character = ""

print("Enter comma separated series of numbers: ", end="", flush=True)
char_str = sys.stdin.read(1)
print("Decoded message: ", end="", flush=True)


while char_str not in ("\n", "\r"):
  number = int(char_str)
  char_str = sys.stdin.read(1)

  while char_str not in ("\n", "\r", ","):
    number = number * 10 + int(char_str)
    char_str = sys.stdin.read(1)

  skip_print = False
  if mode == "UPPERCASE":
    number = number % 27
    output_character = chr(number + ord("A") - 1)
    if number == 0:
      mode = "LOWERCASE"
      skip_print = True
  elif mode == "LOWERCASE":
    number = number % 27
    output_character = chr(number + ord("a") - 1)
    if number == 0:
      mode = "PUNCTUATION"
      skip_print = True
  elif mode == "PUNCTUATION":
    if number == 0:
      mode = "UPPERCASE"
      skip_print = True
    else:
      punctuations_dict = {
        1: "!", 2: "?", 3: ",", 4: ".",
        5: " ",6: ";", 7: '"', 9: "'"
      }
      output_character = punctuations_dict.get(number, '')

  if not skip_print:
    print(output_character, end="", flush=True)

  if char_str not in ("\n", "\r"):
    char_str = sys.stdin.read(1)

print()

