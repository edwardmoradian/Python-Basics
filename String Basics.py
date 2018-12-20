
## Strings are sequences -> slicing, indexing, *, use them in for loops,
## in and not, testing methods, searching methods, modification methods

def main():
    s = "How now brown cow?"
    
    for c in s:
        print(c, end="")
        
    print()
    print(s)
    print(s[4])
    
    # strings are immutable, so this doesn't work
    # s[4] = "c"
    # print(s)

    # slicing
    t = s[-4:-1]
    print(s,t)
    
    # len works
    print(len(s))

    # concatenation: '+', '+='
    f = "John"
    l = "Dow"
    fl = f + l
    print(f,l,fl)
    f += l
    print(f,l)

main()