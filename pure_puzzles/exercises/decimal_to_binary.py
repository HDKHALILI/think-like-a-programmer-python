num = int(input("Enter a number to convert to binary: "))
binary = ''

while num > 0:
  binary = str(num % 2) + binary  
  num = num // 2

print(f"Binary: {binary}")


