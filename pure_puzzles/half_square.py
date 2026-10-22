
# Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like half of a perfect 5 × 5 square (or a right triangle):#####
# ####
# ###
# ##
# #

for row in range(1, 6):
  for _ in range(6 - row):
    print("#", end="")
  print("\n")