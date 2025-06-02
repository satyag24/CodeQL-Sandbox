def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
try:
    number = int(input("Enter a positive integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}.")
except ValueError:
    print("Please enter a valid integer.")
