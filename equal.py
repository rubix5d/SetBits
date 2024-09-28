# z = int(input("Enter number for z"))
# x = int(input("Enter number for x"))



# def equalNumbers(z, x):
#     if z ^ x == 0:
#         print("Numbers are equal")
#     else:
#         print("Numbers are not equal")

# equalNumbers(z,x)

def find_odd_occurence(lst):
    result = 0
    for num in lst:
        result = result ^ num
    return result

print([1,1,2,3,3])