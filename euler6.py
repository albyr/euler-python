# Problem:
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Initialise variables
sumSquares = 0
sumSquared = 0

for i in range (1,101):
    sumSquares += i**2
print (str(sumSquares))

for j in range (1,101):
    sumSquared += j
sumSquared = sumSquared**2

answer = sumSquared - sumSquares
print ("The answer is " + str(answer))
