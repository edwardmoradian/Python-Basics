# read lines from a file
# steps for dealing with files
# 1. Open the file (r,w,a)
# 2. Process the file
# 3. Close the file ASAP.

# open the file
f = open("words.txt", "r")


# process it, remember that the print function adds a newline character - two different ways to remove newline character
line1 = f.readline()    # read the first line
print(line1, end="")            # show it to you
line2 = f.readline()    # read the second line
print(line2, end="")            # show it to you
line3 = f.readline()    # read the thid line
line3 = line3.rstrip("/n")
print(line3)            # show it to you

# close it
f.close()
