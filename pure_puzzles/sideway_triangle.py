
# Write a program that uses only two output statements, print("#") and print("\n"), to produce a pattern of hash symbols shaped like a sideways triangle:
#   #
#   ##
#   ###
#   ####
#   ###
#   ##
#   #

# number of lines is 8 so that is 8 iteration
# max number of # symbol used in one line is 4
# our strategy is to subtract empty spaces from 4
# for example for the first line
#   line length is 4 characters and 3 are spaces and one is hash
#   so row is 1 and abs(4 - 1) = 3 then 4 - 3 is 1 therfore, the inner loop
#   for the first iteration of the outer loop runs only once.
# once mid point is reached the number goes negative and abs make sure we have 
# a positive number


for row in range(1, 8):
  num_hash = 4 - abs(4 - row)
  for _ in range(num_hash):
    print("#", end="")
  print("\n", end="")