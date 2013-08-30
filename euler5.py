# Problem:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Note: "evenly divisible" means divisible with no remainder.

# Initialise variables
# Start at 20 because the smallest number evenly divisible by 1-20 cannot be less than 20
i = 20
foundAnswer = False

# This is not a fast method
while foundAnswer == False:
    for testFactor in range (2,21):
        if i % testFactor != 0:
            # print (str(i) + " divided by " + str(testFactor) + " leaves remainder " + str(i % testFactor))
            break
        if testFactor == 20:
            print ("The answer is " + str(i))
            foundAnswer = True
    i = i + 1
