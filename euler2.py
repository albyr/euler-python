# Check I'm able to generate the Fibonacci sequence up to 4000000
# Define variables
a = 1
b = 1
total = 1
answer = 0
# Begin loop
while total <= 4000000:
    print (total)
    total = a + b
    a = b
    b = total
    # Check if current term is even
    if total % 2 == 0:
        # If current term is even, add to total
        answer = answer + total
print (answer)
