
## Dictionaries
## pairs: key, value

def main():
    # let's create a dictionary {}
    d = {(0,1,2,):[1,2,3],0:12, "Monday":45, "Tuesday":52, "Wednesday":47}
    print(d)
    print(len(d),"\n")
        
    # k,v = d.popitem()
    
    print(d["Tuesday"])
    for k in d:
        print(k)
        
    for k in d:
        print(d[k])
    print()
    
    print(d[0])
    print(d[(0,1,2)])
    print(d[(0,1,2)][1])
    
    d[(0,1,2)][1] = 5
    print(d)
    d[(0,1,2)][1] = d[(0,1,2)][2]
    print(d)
    
## Let's add something to the dictionary. Requires a unique key.
    
    d["Grade"] = "A"
    print(d)
    
## let's delete something form the dictionary.
    
    del(d["Monday"])
    print(d)
    
## Let's change something in the dictionary
    
    d["Grade"] = "B"
    print(d)
    
## create an empty dictionary
    
    e = {}
    print(e)
    e["Tom"] = 44
    print(e)
    
main()




































