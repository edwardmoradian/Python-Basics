# ask the user for the file name
# read in lines from a file
# convert them to integers
# we're gonna tell you which
# one is bigger
# why not throw some functions in here too?

def get_file_name():
    fn = input("Enter file name: ")
    return fn

# we'll assume a != b
def find_bigger(a,b):
    if a>b:
        return a
    return b

def read_first_two_values(file_name):
    f = open(file_name, "r")
    num1 = f.readline()
    num2 = f.readline()
    
    num1 = int(num1)
    num2 = int(num2)
    
    f.close()
    
    return num1,num2
    
def main():
    # a,b = read_first_two_values("numbers.txt")
    # print(a,b)
    fn = get_file_name()
    a,b = read_first_two_values(fn)
    bigger = find_bigger(a,b)
    print("The bigger number is", bigger)
    
    
main()


