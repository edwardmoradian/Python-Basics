# concatentation -> joining stuff together

a = [2,4,6]
b = [3,5,7]

# two methods of doing this: one is not really concatenation, the other is

# Method 1: Not really concatenation

print(a,b)
a.append(b)
print(a,b) # fourth element of list a is list b

# Method 2: Concatentation

a = [2,4,6]
print(a,b)

a+=b
print(a,b)

a = [2,4,6]
print(a,b)

c = a + b
print(a,b,c)

# Find the average of the elements in lists a and b

c = a + b   # create the new list
total = 0

for n in c:
    total += n
    
print("The average of the lists: ",total/len(c))