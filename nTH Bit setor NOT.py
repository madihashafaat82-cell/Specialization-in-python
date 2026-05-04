def setOrNOT(number , n):

    if number & ( 1 << (n - 1)):
        print('/n is SET')
    else:
        print('/n is NOT a SET')

number = int(input('Enter your number: '))
n = int(input('Enter a Bit number: '))
setOrNOT(number , n)
    