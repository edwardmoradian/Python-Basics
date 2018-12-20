
# Copying lists

# not like this
a= [8,6,7]
b = a
print(a,b)
a[0] = 4    # changes to a also changes b becuase both refer to the same list
print(a,b)  # a and b are references and are attached to the same sequence object

# Two ways to copy a list correctly
# 1) use a loop and append()
# 2) use concatenation

# Method 1: Use a loop and append

b = []      # create an empty list

for n in a:     # for each number n in list a...
    b.append(n) # append it to target list b
print(a,b)
a[0] = 9
print(a,b)

# Method 2: Concatenation

b = []
b += a  # concatenate

print(a,b)
b[0] = 97
print(a,b)
