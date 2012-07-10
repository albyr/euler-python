# Define total and set equal to zero
total = 0
# Begin loop using counter x
for x in range(0,1000):
    # Divide counter by three and five
    div5 = x/5
    div3 = x/3
    # Begin if loop
    if div5 == int(div5):
        # If the value of div5 is same as integer of div5 then add to total
        total = total + x
    elif div3 == int(div3):
        # If the value of div3 is same as integer of div3 then add to total
        total = total + x
# Print the total
print (total)
