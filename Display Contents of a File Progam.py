# write a program that displays the contents of a file
# no matter how long the file is
# ask the user for the file they want to view:

def main():
    LineCount = 0
    FileName = input("Enter file name: ")
    
    # open the file for reading
    x = open(FileName, "r")
    
    line = x.readline()
    
    while line != "":
        LineCount += 1
        print(line, end="")
        line = x.readline()
        
    x.close()
    
    print("\nFinished. Lines displayed =", LineCount)
    
main()

def main2():
    LineCount = 1
    FileName = input("Enter file name: ")
    
    # open the file for reading
    x = open(FileName, "r")
    
    line = x.readline()
    print(line, end="")
    
    for line in x:
        LineCount += 1
        print(line, end="")
        line = x.readline()
        
    x.close()
    
    print("\nFinished. Lines displayed =", LineCount)
    
main2()