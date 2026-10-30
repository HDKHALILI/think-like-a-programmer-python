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


HALF = 4
WIDTH = 4 * HALF - 2 # minus 2 make sure that the last line has no space in the middle
for row in range(HALF):
  num_hash = row + 1
  shift_spaces = row
  mid_spaces = WIDTH - (2 * num_hash + 2 * shift_spaces)

  for _ in range(shift_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")

  for space in range(mid_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")
  print()

for row in range(HALF):
  top_half_row = HALF - 1 - row  # 3, 2, 1, 0
  num_hash = top_half_row + 1
  shift_spaces = top_half_row
  mid_spaces = WIDTH - (2 * num_hash + 2 * shift_spaces)

  for _ in range(shift_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")

  for space in range(mid_spaces):
    print(" ", end="")

  for _ in range(num_hash):
    print("#", end="")
  print()