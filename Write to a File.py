# let's write some stuff to a file

# 1. open the file
# 2. write to it
# 3. close the file

# 1. let's open the file
fo = open("blah.txt", "w")

# let's write a string to the file
fo.write("Hello")
fo.write("Hello World")

fo.write(str(12) + "\n") # need str for the write method (only accepts strings)

dog = 12
cat = 3.14159
rat = "Pepper"
fo.write(str(dog))
fo.write(str(cat))
fo.write(str(rat))

# close the file
fo.close


# write to a file, using concatenation

f = open("output.txt", "w")

a = "kittycat"

f.write("hello\n")
f.write("world"+"\n")
f.write(a + "\n")

f.close()