##### global variables: a variable defined outside all functions, so it's (potentially) in scope of all functions

dog = 99    # this is a global variable and it's scop is all function defined after it

def spam():
    print(dog)
    
def eggs():
    print(dog)

def change_it():
    global dog
    dog =77     # this means we're working with the global, global dog is now = 77
    print(dog)  # local variable is now a global variable that will print 77
    
def main():
    spam()
    eggs()
    
    print(dog)
    change_it()
    print(dog)  # will print the global variable 77
    
main()