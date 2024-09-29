num = int(input("Write any binary number: "))
digits = [int(x) for x in str(num)]
digits.reverse()
print(digits)

def firststbit():
    global num
    count = 1
    for i in digits:
        if i & 1 == 0:
            count += 1
        elif i & 1 == 1:
            if count == 3:
                print(f"It is at the {count}rd position")
            elif count == 2:
                print(f"It is at the {count}nd position")
            elif count == 1:
                print(f"It is at the {count}st position")
            else:
                print(f"It is at the {count}th position")
            break
            
firststbit()