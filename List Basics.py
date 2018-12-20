
# List is a variable that can hold more than one piece of data

A_list = [8, 6, 7, 5, 3, 0, 9]  # Integer list
print(A_list)

B_list = [1.2, 3.14, 2.77]  # Float list
print(B_list)

C_list = ["Tom", "Harry"]
print (C_list)

D_list = ["Tom", 27, 3.14]
print(D_list)

# Built-in list function to convert into a list

a = list(range(2, 11, 2)) # 2, 4, 6, 8, 10
print(a)

# the repetition operator: *
# [99] * 8 = [99,99,99,99,99,99,99,99]

ListOf99s = [99] * 8
print(ListOf99s)

# lists are mutable - they can change

AListOfNames = ["Tom","Phiiiiil","Harry"]
print(AListOfNames)

AListOfNames[1] = "Phil"
print(AListOfNames)
