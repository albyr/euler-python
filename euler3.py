# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Add the square root function
from math import sqrt

# Set target
# target = 13195
# target = 600851475143

# Function that finds factors of given number
def findfactors(n):
    for i in range(2,int(sqrt(n)+1)):
        if n/i == int(n/i):
            print (i,int(n/i))

# Function that checks if a number is prime
def checkprime(n):
    for i in range(2,int(sqrt(n)+1)):
        if n/i == int(n/i):
            isprime = False
        else:
            isprime = True
    if isprime == True:
        print (repr(n) + " is prime")
    elif isprime == False:
        print (repr(n) + " is not prime")
