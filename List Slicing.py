
# Slicing: Getting a subset or sublist out of a list
AList = [2,4,6,8,10,12]
print(AList[3]) # This will print the 4th element

# Get a slice
print(AList[2:5]) # does not include element 5

# Find the average of the slice of AList elements from 2 through 4
total = 0
for n in AList:
    total +=n
    
average = total/len(AList)
print(average)