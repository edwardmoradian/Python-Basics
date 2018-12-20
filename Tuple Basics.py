
## Tuples: List that can't change, is a sequence. 
## There are two advantages of using a tuple. 
## 1) Retreiving data from a tuple is faster (e.g., slicing).
## 2) It is also a preventive debugging technique. Save yourself from making mistakes of lists that should not change.
# Principle of least privilege - can only access the data that you necessarily need. Have only the security clearances
# that you necessarily need

def main():
    # define a tuple
    t = (8,6,7,5,3)
    # t[0] = 4    # This does not work with tuples
    # Tuples do support indexing and slicing
    print(t)
    for i in t:
        print(i,end="")
    
    print()
    
    total = 0
    for i in t:
        total += i
        
    print(total)
    print(t[1:3])

## Conversion functions: list(), tuple()
    print(t)
    t = list(t)     # copy tuple t and place in a list and delete original tuple t
    print(t)
    t[0] = 4
    t = tuple(t)
    print(t)
    
    t = ([5,6],)
    t[0][0] = 4
    print(t)

main()

