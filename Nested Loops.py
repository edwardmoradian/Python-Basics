##### Nested Loops

# Using while loops, print a field of stars

j = 0
while j < 3:
    i = 0
    while i < 5:
        print("*", end = "")
        i += 1
    print("")
    j+=1

# Using for loops
    
for j in range(3):
    for i in range(5):
        print("*", end = "")
    print("")

