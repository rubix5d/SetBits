num = int(input("Write any binary number: "))
str_num = str(num)
digits = [int(x) for x in str(num)]
digits.reverse()
print(digits)

def firststbit():
    global num
    global str_num
    count = 0
    for i in digits:
        if i & 1 == 1:
            count = count + 1
        else:
            digits.remove(i)
    return count

print(firststbit())