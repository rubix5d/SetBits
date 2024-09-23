num = int(input("Write any binary number: "))
str_num = str(num)
digits = [int(x) for x in str(num)]
digits.reverse()
print(digits)

def firststbit():
    global num
    global str_num
    count = 1
    for i in digits:
        if i & 1 == 0:
            count += 1
        elif i & 1 == 1:
            print(count)
            break

firststbit()