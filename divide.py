def equaltoZero(num):
    if num <= 0:
        return False
    else:
        return (num & (~(num -1))) == num

 print(equaltoZero(14))
