def Bitnumbers(n):
    ones = 0
    zeroes = 0
    while(n):

     if(n&1==1):
        ones+=1
     else:
        zeroes+=1

        # Right shift to the number
     n >>= 1
    print('/n.of ones =',ones,'/n.of zeroes =',zeroes)

number = int(input('Enter your number '))
Bitnumbers(number)        