# Exercise 1
# Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:
#   ########
#    ######
#     ####
#      ##


# We start with 8 hashes
# at each iteration we replace hashes from each sides with spaces
#   first iteration one hashes from each side is replaced by a space
#   iteration two replaces two hashes from each side with the same number of spaces
# we repeat this 4 times

for row in range(5):
  num_spaces = row * 2
  # shift the hashes half number of num_spaces
  for space in range(num_spaces // 2):
    print(" ", end="")

  for hash_num in range(8 - num_spaces):
    print("#", end="")
  print("\n", end="")



