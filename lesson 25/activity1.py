# Program to check if the the number is the power of 2

def power2(number):

    #As the power of 2 will only have 1 set bit, then n-1 & n will always be 0 for any power of 2
    if (number==0):
        return 0
    if ((number & (~(number - 1)))== number):
        return 1
    return 0

number = int(input("Enter your number : "))

if(power2(number)):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")
    