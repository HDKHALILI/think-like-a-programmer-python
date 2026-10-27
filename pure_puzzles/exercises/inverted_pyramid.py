# Using the same rule as the shapes programs from earlier in the chapter (only two output statements—one that outputs the hash mark and one that outputs an end-of-line), write a program that produces the following shape:
#   ########
#    ######
#     ####
#      ##


# We start with 8 hashes
# at each iteration we decrease it by 2
# we repeat this 4 times

for row in range(5):
  # shift the shapes the same number of spaces as row
  for _ in range(row):
    print(" ", end="")

  for _ in range(8 - row * 2):
    print("#", end="")
  print("\n", end="")



