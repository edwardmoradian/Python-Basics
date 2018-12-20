def main():
    d = {"fido":7, "fang":1, "lady":5}
    print(d)
    
    print(d.get("lady","SAD!"))    
    print(d.get("blake","SAD!")) 
    
    print(d.items())
    print(d.keys())
    
    print(d.pop("fang"))
    print(d)
    
    d.clear()
    print(d)

    

main()