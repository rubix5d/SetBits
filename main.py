n = int(input("Enter any number: "))
def setBit(n):
  ones = 0
  zeros = 0
  while (n > 0):
    if (n & 1 == 1):
        ones = ones + 1
    else:
       zeros = zeros + 1
    n = n >> 1
  return ones, zeros

print(setBit(n))