
def powerof4(number):

    if (number & (~(number & (number - 1)))):
      while(number > 1):
        number >>= 1
        count += 1

      if count % 2 == 0:
         return True
      else:
         return False
      
number = int()

