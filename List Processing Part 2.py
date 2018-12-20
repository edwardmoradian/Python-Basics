# an alternative to for loops, use a while to print contents of numbers
Numbers = [8,6,7,5,3,0,9]

i = 0
while i < 7:
    print(Numbers[i], end="")
    i += 1
print()

# Another example, careful of index error, off-by-one error

i = 0
Total = 0
while i < 7:
    Total += Numbers[i]
    i += 1

print("Your total is: ",Total)

# Another example

i = 0
Total = 0
while i < 7:
    Total += Numbers[i]
    i += 2

print("Your total of even subscript elements is: ",Total)