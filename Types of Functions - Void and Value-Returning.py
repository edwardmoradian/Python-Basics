# void functions - no return statement
# value- returning functions - return statement

# a void function
def add(a,b):
    sum=a+b
    print(sum)
    
# a value-returning function
def add_two(a,b):
    sum=a+b
    return sum

def main():
    add(6,3)
    
    you = add_two(5,2)
    print(you)
    
main()
    