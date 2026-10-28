# Exercise 2
# Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:
#      ##
#     ####
#    ######
#   ########
#   ########
#    ######
#     ####
#      ##


for row in range(8):
  num_hash = 9 - abs(7 - (row * 2))
  spaces = (8 - num_hash) // 2

  for space in range(spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")

  print()
