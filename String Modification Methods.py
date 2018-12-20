## Here are some modification methods. Strings support methods for "modifying" strings
## also * operator
## rstrip(), lstrip(), strip(), upper(), lower()
    
def main():
    s = "x"*3 + "Awesome" + "x"*3
    print(s)
    
    t = s.rstrip("x")
    print(s,t)
    
    t = s.lstrip("x")
    print(s,t)
    
    t = s.strip("x")
    print(s,t)
    
    t = s.upper()
    print(s,t)
    
    t = s.lower()
    print(s,t)
    
    
main()