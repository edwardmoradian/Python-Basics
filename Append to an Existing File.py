# (a)append to an existing file
# existing data is preserved
# new data added to the end of the file

f = open("output.txt","a") # open in append mode
f.write("puppydog\n")
f.close()