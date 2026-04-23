# Program to find GCD of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Start from the smaller of the two numbers and work backwards
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"The GCD is: {gcd}")