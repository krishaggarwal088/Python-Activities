# Take input from the user
number = int(input("Enter your number: "))

# Store the original number for comparison later
original_number = number
reversed_number = 0

# Reverse the number
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

# Check if the original number is equal to the reversed number
if original_number == reversed_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")