
# Reading from a file into a list

# Method one, probably the easiest

f = open("in.txt","r")
a_list = f.readlines()
f.close()
print(a_list)

for n in range(len(a_list)):
    a_list[n] = a_list[n].rstrip("\n")
    
print(a_list)

# another method: read a number, convert it to an int and put the int in a list

a_list = []
f = open("numbers2.txt")
line = f.readline()

while line != "":
    a_list.append(int(line))
    line = f.readline()

print(a_list)
print("The biggest number is", max(a_list))
print("The second number in the file is", a_list[1])

f.close()