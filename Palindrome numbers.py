# Program to check if a number is a palindrome
num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp = temp // 10

if num == reverse:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")