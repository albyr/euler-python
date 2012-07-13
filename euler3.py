# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Import the square root function
from math import sqrt

# Initialise variables
factors = []

# Set target
target = 13195
# target = 600851475143

# Function that finds all the factors (not necessarily prime factors) of a given number
def findfactors(n):
    # for i in range(1,int(sqrt(n)+1)):
    for i in range(1,n+1):
        if n/i == int(n/i):
            factors.append(i)

# Function that checks if a number is prime
def checkprime(n):
    # Trial division
    for i in range(2,int(sqrt(n)+1)):
        if n/i == int(n/i):
            # Number gives a remainder upon division and therefore is not prime
            isprime = False
            break
        else:
            isprime = True
    if isprime == True:
        return True
    elif isprime == False:
        return False

# Find and display all factors of target
findfactors(target)
print (factors)

# Check each factor to see if it is prime or compound
for i in range(0,len(factors)):
    print (factors[i])
    # Why can't I call checkprime here, like this? It works in the console.
    checkprime(factors[i])
