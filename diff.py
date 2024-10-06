def flipit(number1, number2):
    flips = 0
    while(number1 > 0 or number2 > 0):
        t1 = number1 & 1
        t2 = number2 & 1
        if t1 != t2:
            flips += 1
        number1 >>= 1
        number2 >>= 1
    return flips

print(flipit(3,2))