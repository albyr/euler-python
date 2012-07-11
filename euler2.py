# Check I'm able to generate the Fibonacci sequence up to 4000000
# Define variables
a = 1
b = 1
total = 1
while total <= 4000000:
    print (total)
    total = a + b
    a = b
    b = total
