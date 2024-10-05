def switch(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a,b)

print(switch(10,9))