number = int(input("Enter your number:"))

digit = len(str(number))

resultnumber = 0

temp = number
while temp > 0:
    digits = temp % 10
    resultnumber += digits**digit
    temp//=10

if number == resultnumber:
    print(number , 'is an Armstrong number')
else:
    print(number , 'is not an Armstrong number')   
