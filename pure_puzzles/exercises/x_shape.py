# Exercise 2
# Using the same rule as the shapes programs from earlier in the chapter
#  (only two output statements—one that outputs the hash mark and one that
#  outputs an end-of-line), write a program that produces the following shape:
#            #
 ##        ##
  ###    ###
   ########
   ########
  ###    ###
 ##        ##
#            #

for row in range(4):
  num_hash = row + 1
  shift_spaces = row
  mid_spaces = 14 - (num_hash * 2 + (shift_spaces * 2))

  for _ in range(shift_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")

  for space in range(mid_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")
  print()

for row in range(4):
  num_hash = 4 - row
  shift_spaces = num_hash - 1
  mid_spaces = 14 - (num_hash * 2 + (shift_spaces * 2))

  for _ in range(shift_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")

  for space in range(mid_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")
  print()