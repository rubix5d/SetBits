#AND returns 1 if both bits are 1
print(7 & 4)
print(bin(10))

#OR RETURNS 1 IF one of the bits are 1
print(7 | 15)

#XOR returns 1 when both bits are different
print(7 ^ 15)

#ASSIGNMENT
a = 3
b = 7
c = 8

and1 = (a & b)
and2 = (c & b)
or1 =  (b | c)
and3 = (or1 & and2)
q = (and3 | and1)

print("Value for q is", bin(q))