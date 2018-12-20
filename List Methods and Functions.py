
# Let's look at some useful functions and methods for dealing with lists
# Methods: append, remove, sort, reverse, insert, index
# Access objects with dot operator
# Built-in functions: del, min, max

# Append = add items to an existing list at the end of the list
# takes the item you want added as an argument

a = [8,6,7]
print(a)

a.append(4)     # add a 4 to the end of the list
a.append(3)
print(a)

# Index = Takes an value you want to search for in the list as an argument
# If it's found , returns the index where it's found. If it's not found, it will raise an exception.

index = a.index(6)
print(index)

index = a.index(-1)
print(index)

# Insert = Another way to grow your list, but this let's you specify where the new item goes.
# moves everyone over one space to make room.

print(a)
a.insert(1,12)
print(a)

# Sort = Arranges the values in the list in ascending order.

a.sort()
print(a)

# Remove = the first way we can remove something from a list
# Take a copy of the value you want to remove from the list as it's argument
# Removes the first copy it finds starting at element 0

a.remove(7)
print(a)

# Reverse = puts the list in reverse order

a.reverse()
print(a)

# Del = a built-in function that can be used to remove items in a list by index

del(a[3])
print(a)

# Min = a built-in function that takes a list as an argument and returns the smallest value in the list

smallest = min(a)
print("The smallest value in the list is", smallest)

# Max = a built-in function that takes a list as an argument and returns the biggest value in the list

biggest = max(a)
print("The biggest value in the list is", biggest)
















