# Problem:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Import square root function
from math import sqrt

# Initialise variables
checkIsPrime = 1
primeCount = 0

# Function (better than that used in problem 3) to check whether a number is prime
def checkPrime(n):
    if n < 2:
        return False # 0 and 1 are not prime numbers
    if n == 2:
        return True # 2 is the first prime number
    elif n % 2 == 0:
        return False # No even numbers (other than 2) are prime numbers
    for i in range(3,int(n**0.5)+1,2): # Only checks odd numbers, starting at 3
        if n % i == 0:
            # n mod i is equal to zero and therefore n cannot be prime
            return False
    # n is not 0, 1, 2 and does not have any factors other than 1 or itself and is therefore prime
    return True

while primeCount != 10001:
    print ("Checking " + str(checkIsPrime))
    if checkPrime(checkIsPrime) == True:
        primeCount += 1
        print (str(checkIsPrime) + " is prime number " + str(primeCount))
    if primeCount == 10001:
        break
    else:
        checkIsPrime += 1
print (str(checkIsPrime) + " is prime number " + str(primeCount))
