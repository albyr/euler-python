# Problem:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Initialise variables
palindromes = []

# Function that checks if a number is palindromic
def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        palindromic = True
    else:
        palindromic = False
    return palindromic

# This is an incredibly slow way of doing this. Needs fixing.
# Loop through x and y from 100 to 999
for x in range(100,1000):
    for y in range(100,1000):
        z = x * y
        # Is z a palindrome?
        check = isPalindrome(z)
        if check == True:
            # Add z to the list of palindromes
            palindromes.append(z)

# Find the largest palindrome and print it out
print ("The largest palindrome is " + str(max(palindromes)))
