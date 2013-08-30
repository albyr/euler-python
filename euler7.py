# Problem:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# Import square root function
from math import sqrt

# Initialise variables
checkIsPrime = 1
primeCount = 0

# Function (re-used from problem 3) to check whether a number is prime
def checkprime(n):
    # Trial division
    for i in range(2,int(sqrt(n)+2)):
        if n < 2:
            isPrime = False
        elif n == 2:
            isPrime = True
        elif n % i == 0:
            # n mod i is equal to zero and therefore n is not prime
            isPrime = False
            # Exit loop to prevent isprime from subsequently being set true
            break
        elif n % i != 0:
            # n might be prime, so set isprime equal to true
            isPrime = True
    return isPrime

while primeCount != 10001:
    if checkprime(checkIsPrime) == True:
        primeCount += 1
    if primeCount == 10001:
        break
    else:
        checkIsPrime += 1
print (str(checkIsPrime) + " is prime number " + str(primeCount))
