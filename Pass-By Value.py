##### pass by value: what you do to the parameter, you do to the parameter

def change_it(cat):
    print("cat=", cat)
    cat =99
    print("cat=",cat)
    
def main():
    x=11
    print("x=", x)
    change_it(x)
    print("x=",x)

main()