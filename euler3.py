# Problem:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Import the square root function
from math import sqrt
# Import date and time function for logging
import datetime

# Initialise variables
factors = []
nonprimefactors = []

# Set target
# target = 13195
# target = 31667149
target = 600851475143

# Function that finds all the factors (not necessarily prime factors) of a given number
def findfactors(n):
    # Output log data
    print ("Factoring " + repr(n))
    for i in range(2,int(sqrt(n)+1)):
        if n/i == int(n/i):
            factors.append(i)
            factors.append(int(n/i))

# Function that checks if a number is prime
def checkprime(n):
    # Trial division
    for i in range(2,int(sqrt(n)+2)):
        if n % i == 0:
            # n mod i is equal to zero and therefore n is not prime
            isprime = False
            # Exit loop to prevent isprime from subsequently being set true
            break
        elif n % i != 0:
            # n might be prime, so set isprime equal to true
            isprime = True
    return isprime

# Function that removes the contents of one list from another
def filterlist(fulllist, toexclude):
    excludedfactors = set(toexclude)
    return (x for x in fulllist if x not in excludedfactors)

print ("Beginning search ...")
starttime = datetime.datetime.now()
print (str(starttime))

# Find and display all factors of target
findfactors(target)
print ("Initial list of factors: " + repr(sorted(factors)))

# Search for non-prime factors
for i in range(0,len(factors)):
    # Output log data
    print ("Checking " + repr(factors[i]))
    if checkprime(factors[i]) == False:
        # Factor is not prime
        # Add non-prime factor to list of non-prime factors
        nonprimefactors.append(factors[i])
        # Add factors of non-prime factor to list of factors
        findfactors(factors[i])
            
# Remove duplicates from both lists
factors = list(set(factors))
nonprimefactors = list(set(nonprimefactors))
# Output log data
print ("All factors: " + repr(sorted(factors)))
print ("Non-prime factors: " + repr(sorted(factors)))

# Remove non-prime factors from list of factors
primefactors = list(filterlist(factors, nonprimefactors))
# Return the largest prime factor
print ("The largest prime factor of " + repr(target) + " is " + repr(max(primefactors)) + ".")

# How long did this take?
endtime = datetime.datetime.now()
print ("Started at " + str(starttime))
print ("Ended at " + str(endtime))
