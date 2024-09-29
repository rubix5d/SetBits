num = input("Enter any binary number")
num = [str(x) for x in str(num)]
def rev():
    my_string = ""
    num.reverse()
    for x in num:
        my_string += ''+x
    return my_string
print(rev())