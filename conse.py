
def longconsecutive():
   print("Enter any binary number")
   arr = list(map(str, input("").split()))
   print("Max Consecutive : ", len(max("".join(map(str, arr)).split("0"))))

longconsecutive()
