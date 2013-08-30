# Problem:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Initialise variables
palindromes = []

# Import date and time function for logging
import datetime

# Function that checks if a number is palindromic
def isPalindrome(n):
    # Uses extended slice syntax, without start or end and with step -1, to reverse string representation of n
    if str(n) == str(n)[::-1]:
        palindromic = True
    else:
        palindromic = False
    return palindromic

# This is an incredibly slow way of doing this. Needs fixing.
starttime = datetime.datetime.now()
# Generate all possible products of two 3-digit numbers
for x in range(100,1000):
    # Only need to check from x to 1000 because otherwise we repeat calculations
    for y in range(x,1000):
        z = x * y
        # Is z a palindrome?
        check = isPalindrome(z)
        if check == True:
            # Add z to the list of palindromes
            palindromes.append(z)

# Find the largest palindrome and print it out
print ("The largest palindrome is " + str(max(palindromes)))
print (datetime.datetime.now()-starttime)
