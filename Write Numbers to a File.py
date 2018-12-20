# Write some numbers to a file
a = 55
b = 13
f = open("nums.txt","w")

f.write(str(a) + "\n")
f.write(str(b) + "\n") # str converts numbers into strings

f.close()